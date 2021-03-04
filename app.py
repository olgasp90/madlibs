from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some_secret_password'
debug = DebugToolbarExtension(app)


@app.route('/home')
def ask_user():
    """ create and show the form """
    user_input = story.prompts
    return render_template("questions.html", prompts = user_input)


@app.route('/story')
def generate_story():
    """create a story"""
    content = story.generate(request.args)
    return render_template('story.html', story = content)

