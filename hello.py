from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
	return "changed index page"



@app.route("/hello")
def hello():
    return "hello world"

if __name__ == "__main__":
    app.run()