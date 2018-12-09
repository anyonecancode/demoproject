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
    #Pagination support
    page = request.args.get('page', 1, type=int)
    title = 'Explore'
    section = 'explore'
    template = 'searchresults.html'
    #Default query. Simple SELECT FROM beers if no filter or sort, and the base we join against otherwise.
    base_query = Beer.query

    #We'll need to do some if we filter and/or sort, but we want to make sure we only join on a given
    #Model once, hence the set data structure
    joined_models = set()

    #filterparams = request.args.getlist('filterby', str)
    #f, joined_models = _buildFilterByQuery(base_query, filterparams, joined_models)

    orderby = request.args.get('orderby', None, str)
    base_query, joined_models = _buildOrderyByQuery(base_query, orderby, joined_models)

    for m in joined_models:
        base_query =  base_query.join(m)

    count = base_query.count()
    pagination = base_query.paginate(page,25, error_out=False)

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


def _buildFilterByQuery(baseQuery, filterparams, joined_models):
    if filterparams is None:
        return baseQuery, joined_models
    return baseQuery, joined_models




def _buildOrderyByQuery(base_query, orderby_param, joined_models = set()):
    orderby = Beer.name #Default

    if orderby_param is None:
        return base_query.order_by(orderby.asc()), joined_models

    orderDesc = False
    if orderby_param[0] == '-':
        orderDesc = True
        orderby_param = orderby_param[1:]


    if orderby_param == 'category':
        joined_models.add(Category)
        orderby = Category.name
    if orderby_param == 'brewery':
        joined_models.add(Brewery)
        orderby = Brewery.name
    if orderby_param == 'region':
        joined_models.add(Brewery)
        orderby = Brewery.state
    if orderby_param == 'country':
        joined_models.add(Brewery)
        orderby = Brewery.country

    if orderDesc:
        orderby = orderby.desc()

    return base_query.order_by(orderby), joined_models


