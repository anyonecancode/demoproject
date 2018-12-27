from flask import render_template, request, url_for
from app import app
from app.models import Beer, Category, Brewery
from collections import defaultdict
from itertools import chain

#Routing constants
VIEWS = {
    'home': {
        'template': 'index.html'
        ,'section': 'home'
        ,'title': None
        }
    ,'explore': {
        'template': 'searchresults.html'
        ,'section': 'browse'
        ,'title': 'Explore'
        }
    }

#Pagination constants
#In a larger app, might go in separate config or constants file, but
#the current app is small enough it makes more sense to keep it closer
#to where it is used
MAX_RESULTS_PER_PAGE = 25

@app.route('/')
def index():
    return render_template(
            VIEWS['home']['template']
            ,section=VIEWS['home']['section'])


@app.route('/explore')
def explore():
    #Pagination support
    page = request.args.get('page', 1, type=int)

    #Default query. Simple SELECT FROM beers if no filter or sort, and the base we join against otherwise.
    query = Beer.query

    #Filtering and sorting requires setting up some table joins. Determine what the joins are and,
    #while we're at it, prep our data for applying soting and filtering a few lines later
    filterargs = request.args.getlist('filterby', str)
    orderarg = request.args.get('orderby', None, str)
    joined_models, filterkeys, orderby = _extractFromRequestargs(filterargs, orderarg)
    for m in joined_models:
        query =  query.join(m)

    #Apply filters, if any
    query = _applyFilters(query, filterkeys)

    #Apply ordering (default to by beer name ASC if none)
    query = _applyOrdering(query, orderby)

    results = query.paginate(page,MAX_RESULTS_PER_PAGE, error_out=False)

    pager = {
            'prev': url_for('explore',
                page=results.prev_num
                ,orderby=orderarg
                ,filterby=filterargs
                ) if results.has_prev else None
            ,'next': url_for('explore'
                ,page=results.next_num
                ,orderby=orderarg
                ,filterby=filterargs) if results.has_next else None
            ,'orderlink': url_for('explore',q=1,filterby=filterargs)
            }

    return render_template(
            VIEWS['explore']['template']
            ,section=VIEWS['explore']['section']
            ,title=VIEWS['explore']['title']
            ,results = results
            ,pager = pager
            ,ordered_by = orderarg if orderarg else 'beer'
            ,filtered_by = filterargs)


def _extractFromRequestargs(filterargs, orderarg):
    joined_models = set()
    filterkeys = defaultdict(list)
    orderby = [Beer.name, False]

    for param in filterargs:
        key, *value = param.split('|', 1)

        if not value:
            continue

        filterkeys[key].append(value)
        if key.lower() == 'category':
            joined_models.add(Category)
        if key.lower() in ['region', 'countries']:
            joined_models.add(Brewery)

    if orderarg:
        if orderarg[0] == '-':
            orderby[1] = True
            orderarg = orderarg[1:]

        if orderarg == 'category':
            joined_models.add(Category)
            orderby[0] = Category.name
        if orderarg == 'brewery':
            joined_models.add(Brewery)
            orderby[0] = Brewery.name
        if orderarg == 'region':
            joined_models.add(Brewery)
            orderby[0] = Brewery.state
        if orderarg == 'country':
            joined_models.add(Brewery)
            orderby[0] = Brewery.country
    orderby = orderby[0].desc() if orderby[1] else orderby[0].asc()

    return joined_models, filterkeys, orderby


def _applyFilters(query, filterkeys):
    if len(filterkeys) < 1:
        return query
    for k in filterkeys:
        v = filterkeys[k]
        if k == 'category':
           if len(v) > 1:
                query = query.filter(Category.name.in_(v))
           else:
                query = query.filter(Category.name == v[0])
        if k == 'region':
           if len(v) > 1:
                query = query.filter(Brewery.state.in_(v))
           else:
                query = query.filter(Brewery.state == v[0])
        if k == 'countries':
            countries =  [i[0].split(';') for i in v]
            countries = (list(chain.from_iterable(countries)))
            query = query.filter(Brewery.country.in_(countries))
    return query


def _applyOrdering(query, orderby):
    return query.order_by(orderby)
