# app.py
from flask import Flask  # import flask

from models import Schema

from service import ToDoService
app = Flask(__name__)             # create an app instance


@app.route("/")
def hello():
    return "Hello World"

@app.route("/eder")
def hello_name(eder, name="eder"):
    return "Hello " + name

#@app.route("/todo", method=["POST"])                   # at the end point /
#def create_todo():
#    return ToDoService().create(request.get_json())

def hello():                      # call method hello
    return "Hello World!"         # which returns "hello world"

if __name__ == "__main__":        # on running python app.py
    Schema()
    app.run(debug=True, host='0.0.0.0', port=8080)                     # run the flask app