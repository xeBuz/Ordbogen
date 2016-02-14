import os
basedir = os.path.abspath(os.path.dirname(__file__))
database_path = "/database/"


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class Development(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir + database_path, 'app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


class Production(Config):
    pass


class Testing(Config):
    TESTING = True


