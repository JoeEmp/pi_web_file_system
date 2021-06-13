#!/bin/bash
kill -9 `lsof -ti:5000`
source venv3x/bin/activate
nohup  python3 app.py $1 &
