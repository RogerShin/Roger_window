from flask import Flask

app = Flask(__name__)


# Use the route() decorator to bind a function to a URL.
@app.route("/")
def index():
    return "<h1>我的主題</h1>\n<h2>職能發展學院</h2>"

# route("/")
@app.route("/hello")
def hello():
    return '<h1>Hello, World</h1>'