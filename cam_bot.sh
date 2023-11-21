#!/bin/bash

cd /home/tkoval/git-local/tk/cam-bot
source "$( /home/tkoval/.local/bin/poetry env info --path )/bin/activate"
python app/main.py