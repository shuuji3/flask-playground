from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/user/<username>')
def show_user_profile(username):
    """Show the user profile for that user."""
    return f'User {escape(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    """Show the post with the given id, the id is an integer."""
    return f'Post #{post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    """Show the subpath after /path"""
    return f'Subpath {escape(subpath)}'


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


def do_the_login():
    return 'You logged in'


def show_the_login_form():
    return 'Login form'
