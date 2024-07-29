#!/bin/sh

# start gunicorn server

python -m gunicorn app:app --config gunicorn.conf.py
