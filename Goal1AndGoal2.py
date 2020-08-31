from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "Users.db"))

app = Flask(__name__,template_folder='./')
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

class User(db.Model):
    uname = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "Name of user : {}".format(self.uname)

@app.route('/')
def upload_file_front():
    return render_template('Goal1AndGoal2.html')

def countNames(filname):
    count=0
    with open(filname) as fp:
        while True:
            line = fp.readline()
            user = User(uname=line)
            db.session.add(user)
            db.session.commit()
            if not line:
                break
            e=line.strip()
            e = e.split(' ')[-1]
            if (e == "siddique"):
                count = count + 1
    return count

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        c=countNames(f.filename)
        return 'Total siddique appear in last names are : '+str(c)

@app.route('/names', methods=['GET', 'POST'])
def filenames_saved():
    users = User.query.all()
    return render_template('UserNames.html',Users=users)
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)