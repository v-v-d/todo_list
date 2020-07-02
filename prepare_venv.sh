#!/bin/sh

echo 'create python venv'

sudo apt-get install python3-venv

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r ./todo_api/requirements.txt
