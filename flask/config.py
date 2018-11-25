import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'

    DB_USER = os.environ.get('DB_USER') or 'root'
    DB_PASS = os.environ.get('DB_PASS') or 'pass'
    DB_HOST = os.environ.get('DB_HOST') or '127.0.0.1'
    DB_PORT = os.environ.get('DB_PORT') or '3306'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://{user}:{pw}@{host}/openbeerdb'.format(user = DB_USER, pw = DB_PASS, host = DB_HOST)
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #        'sqlite:///' + os.path.join(basedir, 'app.db')
