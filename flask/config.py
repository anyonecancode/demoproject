import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'

    DB_USER = os.environ.get('DB_USER') or 'db_user'
    DB_PASS = os.environ.get('DB_PASS') or 'db_pass'
    DB_HOST = os.environ.get('DB_HOST') or '127.0.0.1'
    DB_PORT = os.environ.get('DB_PORT') or '5432'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://{user}:{pw}@{host}/openbeerdb'.format(user = DB_USER, pw = DB_PASS, host = DB_HOST)
