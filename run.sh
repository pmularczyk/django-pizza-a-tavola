#!/usr/bin/bash

# upgrade pip
python -m pip install --upgrade pip

# install pipenv
pip install pipenv

# within project - next to requirements.txt
# automatically install requirements from .txt file if available
pipenv install

# start django project (next to .env file to load environment variables)
pipenv run python store/manage.py runserver
