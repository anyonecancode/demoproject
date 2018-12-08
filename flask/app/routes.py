from flask import render_template, request, url_for
from app import app
from app.models import Beer, Category, Brewery

@app.route('/')
def index():
    return render_template('index.html', section='home')


@app.route('/explore')
@app.route('/explore/<category>')
@app.route('/explore/<category>/<style>')
def explore(category = None, style = None):
    page = request.args.get('page', 1, type=int)
    title = 'Explore'
    section = 'explore'
    template = 'searchresults.html'

    q = Beer.query
    orderby = Beer.name
    orderDesc = False
    orderbyField = None

    orderbyparam = request.args.get('orderby', None, str)
    if (orderbyparam):
        parts = orderbyparam.split('|')
        orderbyField = parts[0]
        if len(parts) == 2 and parts[1].lower() == 'desc':
            orderDesc = True

    if orderbyField:
        if orderbyField == 'category':
            q = q.join(Category)
            orderby = Category.name
        if orderbyField == 'brewery':
            q = q.join(Brewery)
            orderby = Brewery.name
        if orderbyField == 'region':
            q = q.join(Brewery)
            orderby = Brewery.state
        if orderbyField == 'country':
            q = q.join(Brewery)
            orderby = Brewery.country

    if orderDesc:
        orderby = orderby.desc()

    q = q.order_by(orderby)

    count = q.count()
    pagination = q.paginate(page,25)

    results = []
    for beer in pagination.items:
        results.append({
            'beer': beer.name
            ,'category': beer.category
            ,'style': beer.style
            ,'abv': beer.abv
            ,'brewery': beer.brewery
                })

    pagecontrols = {
            'resultscount': count
            ,'page': pagination.page
            ,'pages': pagination.pages
            ,'prev': url_for('explore', page=pagination.prev_num) if pagination.has_prev else None
            ,'next': url_for('explore', page=pagination.next_num) if pagination.has_next else None
            }
    print(pagecontrols['next'])
    return render_template(template, title = title, section = 'explore', results = results, pagecontrols = pagecontrols)
