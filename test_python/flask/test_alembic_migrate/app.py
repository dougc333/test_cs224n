from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    age = db.Column(db.Integer)

@app.route('/test')
def test():
    return "index here"

@app.route('/')
def index():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route("/add")
def add():
    return render_template('add_user.html')

#this is incorrect...put this into lambda fn
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    print("1")
    print("request.method",request.method)
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        age = request.form['age']
        user = User(username=username, email=email, age=age)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        print("GET")
        return render_template('add_user.html')


@app.route('/delete_users', methods=['POST'])
def delete_users():
    db.drop_all()
    db.create_all()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)