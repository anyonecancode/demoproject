from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html', section='home')


@app.route('/explore')
@app.route('/explore/<category>')
@app.route('/explore/<category>/<style>')
def explore(category = None, style = None):
    title = 'Explore'
    section = 'explore'
    template = 'searchresults.html'

    return render_template(template, title = title, section = 'explore')
