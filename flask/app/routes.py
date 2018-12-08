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

    orderby = request.args.get('orderby', None, str)
    q = _buildOrderyByQuery(q, orderby)

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
            ,'prev': url_for('explore', page=pagination.prev_num, orderby=orderby) if pagination.has_prev else None
            ,'next': url_for('explore', page=pagination.next_num, orderby=orderby) if pagination.has_next else None
            }
    print(pagecontrols['next'])
    return render_template(template, title = title, section = 'explore', results = results, pagecontrols = pagecontrols)


def _buildOrderyByQuery(baseQuery, orderbyparams):
    orderby = Beer.name #Default

    if orderbyparams is None:
        return baseQuery.order_by(orderby.asc())

    parts = orderbyparams.split('|')
    orderbyField = parts[0]
    orderDesc = True if (len(parts) == 2 and parts[1].lower() == 'desc') else False

    if orderbyField == 'category':
        baseQuery = baseQuery.join(Category)
        orderby = Category.name
    if orderbyField == 'brewery':
        baseQuery = baseQuery.join(Brewery)
        orderby = Brewery.name
    if orderbyField == 'country':
        baseQuery = baseQuery.join(Brewery)
        orderby = Brewery.country

    if orderDesc:
        orderby = orderby.desc()

    return baseQuery.order_by(orderby)
