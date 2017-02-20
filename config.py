#coding:utf8

DB_USERNAME = 'csdnblog'
DB_PASSWORD = '123456'
DB_HOSTNAME = 'localhost'
DB_DATABASE = 'csdn_blog'

class Config(object):
    """Base config class."""
    pass

class ProdConfig(Config):
    """Production config class."""
    pass

class Devconfig(Config):
    """Devlopment config class."""
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}'.format(DB_USERNAME, DB_PASSWORD, DB_HOSTNAME, DB_DATABASE)

