kill -9 `lsof -ti:10086`
nohup  python3 app.py debug &
