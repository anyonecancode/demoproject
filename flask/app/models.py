from app import db

class Beer(db.Model):
    __tablename__ = 'beers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    brewery_id = db.Column(db.Integer)
    cat_id = db.Column(db.Integer)
    style_id = db.Column(db.Integer)
    abv = db.Column(db.Float)
    ibu = db.Column(db.Float)
    upc = db.Column(db.Integer)
    filepath = db.Column(db.String(255))
    descript = db.Column(db.Text())
    add_user = db.Column(db.Integer)
    last_mod = db.Column(db.DateTime)

    def __repr__(self):
        return '<Beer {}>'.format(self.name)


class Brewery(db.Model):
    __tablename__ = 'breweries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    address1 = db.Column(db.String(255))
    address2 = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    code = db.Column(db.String(255))
    country = db.Column(db.String(255))
    phone = db.Column(db.String(50))
    website = db.Column(db.String(255))
    filepath = db.Column(db.String(255))
    descript = db.Column(db.Text())
    add_user = db.Column(db.Integer)
    last_mod = db.Column(db.DateTime)

    def __repr__(self):
        return '<Brewery {}>'.format(self.name)

class BreweryGeocode(db.Model):
    __tablename__ = 'breweries_geocode'
    id = db.Column(db.Integer, primary_key=True)
    brewery_id = db.Column(db.Integer)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    accuracy = db.Column(db.String(255))


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('cat_name', db.String(255))
    last_mod = db.Column(db.DateTime)

    def __repr__(self):
        return '<Category {}>'.format(self.name)

class Style(db.Model):
    __tablename__ = 'styles'
    id = db.Column(db.Integer, primary_key=True)
    cat_id = db.Column(db.Integer)
    name = db.Column('style_name', db.String(255))
    last_mod = db.Column(db.DateTime)

    def __repr__(self):
        return '<Style {}>'.format(self.name)
