# DB config
DB_HOST = '127.0.0.1'
DB_DATABASE = 'blog'
DB_USERNAME = 'blog'
DB_PASSWORD = '123456'


class Config(object):

    '''Base config class.'''
    pass


class ProdConfig(Config):

    '''Production config class.'''
    pass


class DevConfig(Config):

    '''Development config class.'''
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}'.format(
        DB_USERNAME, DB_PASSWORD, DB_HOST, DB_DATABASE)
