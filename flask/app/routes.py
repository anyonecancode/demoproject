from flask import render_template
from app import app
from app.models import Beer

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

    beers = Beer.query.all()

    results = []
    for b in beers:
        results.append({
            'beer': b.name
            ,'category': b.category
            ,'style': b.style
            ,'abv': b.abv
            ,'brewery': b.brewery
                })

    return render_template(template, title = title, section = 'explore', results = results)
