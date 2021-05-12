kill -9 `lsof -ti:5000`
nohup  python3 app.py $1 &
