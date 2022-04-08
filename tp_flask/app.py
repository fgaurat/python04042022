from flask import Flask

from TodoDAO import TodoDAO

app = Flask(__name__)

@app.route("/")
def index():
    dao = TodoDAO(r'..\data\todos_db.db')
    list_todos="<ul>"
    for todo in dao.findAll():
        list_todos+=f"<li>{todo.title}</li>"
    list_todos+="</ul>"


    return "<a href='/hello'>Hello, World!</a><br/>"+list_todos

@app.route("/hello")
def hello_world():
    return "<p>l'autre Hello, World!</p>"