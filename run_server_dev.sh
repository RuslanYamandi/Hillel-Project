#!/bin/bash

python3 src/manage.py migrate
python3 src/manage.py check
python3 src/manage.py runserver 0:8000