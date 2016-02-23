import os
basedir = os.path.abspath(os.path.dirname(__file__))
database_path = basedir + "/database/"


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class Development(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(database_path, 'app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


class Production(Config):
    DEBUG = False
    TESTING = False


class Testing(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(database_path, 'testing.db')



