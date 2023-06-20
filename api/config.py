# REST API 2023
#
# This project has no License, which means that this work is under
# exclusive copyright by default. More details in:
#
# https://choosealicense.com/no-permission/
#
# AUTHORS:
# Luan Bruno Domingues de Oliveira

"""
Flask configuration file
"""

import os

basedir = os.path.abspath(path="./")


class Config:
    UPLOAD_FOLDER = "uploads"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + basedir + "/instance/api.sqlite3"
    MONGO_URI = "mongodb://127.0.0.1:27017/api"


class DevConfig(Config):
    FLASK_ENV = "development"
    FLASK_DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProdConfig(Config):
    FLASK_ENV = "production"
    FLASK_DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
