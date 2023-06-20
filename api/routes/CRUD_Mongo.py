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
Routes to create, read, update and delete objects in MongoDB from API.
"""

from flask import Blueprint, request

from ..database.MongoDB import utils


bp = Blueprint(name="CRUD_Mongo", import_name=__name__)


@bp.route("/MongoDB/create", methods=["POST"])
def create():
    response = utils.create(request=request.json)
    if response == None:
        return {}, 500
    return response, 200


@bp.route("/MongoDB/read_all", methods=["GET"])
def read_all():
    response = utils.read_all()
    if response == None:
        return {}, 500
    return {"Documents": response}, 200


@bp.route("/MongoDB/read/<string:id>", methods=["GET"])
def read(id: str):
    response = utils.read(id=id)
    if response == None:
        return {}, 500
    return {"Document": response}, 200


@bp.route("/MongoDB/update/<string:id>", methods=["PUT"])
def update(id: str):
    response = utils.update(id=id, request=request.json)
    if response == None:
        return {}, 500
    return {"Document": response}, 200


@bp.route("/MongoDB/delete/<string:id>", methods=["DELETE"])
def delete(id: str):
    response = utils.delete(id=id)
    if response == None:
        return {}, 500
    return {"Document": response}, 200
