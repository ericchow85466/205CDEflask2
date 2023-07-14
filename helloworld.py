from flask import Flask

app=flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello 205CDE!'