# simple flask app to test the API
from flask import Flask, jsonify, request

from models import FlashcardModel
from queries import (
    create_flashcard,
    delete_flashcard,
    get_flashcard,
    get_flashcards,
    update_flashcard,
)
from tasks import add

app = Flask(__name__)


@app.route("/api", methods=["GET"])
def api():
    data = request.get_json()
    return jsonify(data)


# add task and return task id
@app.route("/add", methods=["POST"])
def add_task():
    data = request.get_json()
    task = add.delay(data["x"], data["y"])
    return jsonify({"task_id": task.id})


# get results of the task or status
@app.route("/task/<task_id>", methods=["GET"])
def task(task_id):
    task = add.AsyncResult(task_id)
    if task.ready():
        return jsonify({"status": task.status, "result": task.get()})
    else:
        return jsonify({"status": task.status})


# get all flashcards
@app.route("/flashcards", methods=["GET"])
def flashcards():
    return jsonify(get_flashcards())


# create a flashcard
@app.route("/flashcards", methods=["POST"])
def create():
    data = request.get_json()
    flashcard = create_flashcard(FlashcardModel(**data))
    return jsonify(flashcard)


if __name__ == "__main__":
    app.run(debug=True)
