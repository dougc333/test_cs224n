
from flask import Flask
from flask import send_from_directory
app = Flask(__name__,
            static_url_path='/public')

@app.route("/")
def hi():
  return "hi"

if __name__ == "__main__":
	app.run(debug=True)

