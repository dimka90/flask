from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello():
    return "Hello World,Coding is Really fun"
app.run()
