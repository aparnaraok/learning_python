from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>/<lastname>')

def hello_name(name, lastname):
    return 'Hello %s Welcome %s!'%(name, lastname)

if __name__ == '__main__':
    app.run(debug=True)

#http://127.0.0.1:5000/hello/aparna
#Hello aparna!

#http://127.0.0.1:5000/hello/aparna/kota
#Hello aparna Welcome kota!