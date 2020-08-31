from flask import Flask, render_template, request
import os
from flask_sqlalchemy import SQLAlchemy
import json
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "Todo.db"))

app = Flask(__name__,template_folder='./')
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer , primary_key=True , autoincrement=True)
    title = db.Column(db.String(80))

    def __repr__(self):
        return "Task : {}".format(self.title)

@app.route('/todo/create', methods=['GET'])
def create_todo():
    todoTitle = request.args.get('title', type=str)
    todo = Todo(title=todoTitle)
    db.session.add(todo)
    db.session.commit()
    return {"success":"1"}

@app.route('/todo/delete', methods=['GET'])
def delte_todo():
    id = request.args.get('id', type=str)
    obj = Todo.query.filter_by(id=id).one()
    db.session.delete(obj)
    db.session.commit()
    return {"success":"1"}

@app.route('/todo/show', methods=['GET'])
def showAll():
    s="0"
    todos = Todo.query.all()
    if(todos):
        s="1"
    todos=[{"id":e.id,"title":e.title}  for e in todos]
    res={"success":s,"result":todos}
    return json.dumps(res)

    return render_template('UserNames.html',Users=users)
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)