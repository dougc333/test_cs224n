from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    print("index")
    return render_template('index.html')

@app.route("/search")
def search():
    print("search")
    return render_template('search.html')