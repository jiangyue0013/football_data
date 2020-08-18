import os
import sys

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):
    DE_MYSQL_USER = os.getenv('DE_MYSQL_USER')
    DE_MYSQL_PASSWORD = os.getenv('DE_MYSQL_PASSWORD')
    DE_MYSQL_HOST = os.getenv('DE_MYSQL_HOST')
    DE_MYSQL_USER_PORT = os.getenv('DE_MYSQL_PORT')
    DE_MYSQL_DB = os.getenv('DE_MYSQL_DB')
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DE_MYSQL_USER}:{DE_MYSQL_PASSWORD}@{DE_MYSQL_HOST}:{DE_MYSQL_USER_PORT}/{DE_MYSQL_DB}'



class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLE = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'  # in-memory database


class ProductionConfig(BaseConfig):
    pass

config = {
    'development': DevConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}