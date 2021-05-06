#!/bin/bash
# activate virtual environment
. ./venv/bin/activate 

# run cgi server
python -m http.server --bind localhost --cgi 8000