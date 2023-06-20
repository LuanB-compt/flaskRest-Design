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
Flask API
"""

__all__ = ["create_app"]

from flask import Flask
from flask_cors import CORS

from .config import DevConfig
from .database.models import MongoDB, SQLite
from .routes import CRUD_Mongo, CRUD_SQLite


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(obj=DevConfig)

    app.register_blueprint(blueprint=CRUD_Mongo.bp)
    app.register_blueprint(blueprint=CRUD_SQLite.bp)

    CORS(app)

    SQLite.db.init_app(app=app)
    MongoDB.mongo_client.init_app(app=app)
    with app.app_context():
        SQLite.db.create_all()
        SQLite.db.session.commit()

        return app
