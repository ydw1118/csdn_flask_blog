#coding:utf8

class Config(object):
    """Base config class."""
    pass

class ProdConfig(Config):
    """Production config class."""
    pass

class Devconfig(Config):
    """Devlopment config class."""
    DEBUG = True

