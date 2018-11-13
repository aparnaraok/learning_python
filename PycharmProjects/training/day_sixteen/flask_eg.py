#import flask
from flask import Flask
app = Flask(__name__)
#@app.route('/hello/') #configured same in django urls.py
@app.route('/hello/<int:postID>')

def hello_world(postID):
    return "Hello World....Welcome to Flask %d!!!"%(postID)

if __name__ == '__main__':
    app.run()
    app.route(rule, options)

#http://127.0.0.1:5000/hello/1
#Hello World....Welcome to Flask 1!!!