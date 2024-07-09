from flask import Flask, render_template

app = Flask(__name__)

# Use the route() decorator to bind a function to a URL.
@app.route("/")
def index():
    return render_template("index.html.jinja")
# route("/")
@app.route("/hello")
def hello():
    return '<h1>Hello, World</h1>'

@app.route("/user/<username>")
def show_user_profile(username):
    # show the user profile for that user
    return f"<h1>Hello! {(username)}<h1/>"

@app.route("/post/<int:post_id>")
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f"<h1>Post {post_id}</h1>"