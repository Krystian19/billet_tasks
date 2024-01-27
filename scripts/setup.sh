#!/bin/sh

tail -f /dev/null

# # install dependencies
pip install -r requirements.txt

# # run the web dev server 
python src/main.py
