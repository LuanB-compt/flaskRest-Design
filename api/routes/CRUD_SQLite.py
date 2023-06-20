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
Routes to create, read, update and delete objects in SQLite from API.
"""

from flask import Blueprint, request

from ..database.models.SQLite import Lecture, Room, Student, db
from ..database.SQLite import utils


bp = Blueprint(name="CRUD_SQLite", import_name=__name__)


# *** CREATE ROUTES ***
@bp.route("/SQL/Room/create", methods=["POST"])
def createRoom():
    result = utils.createRoom(request=request.json)
    if result:
        return {}, 200
    else:
        return {}, 500


@bp.route("/SQL/Student/create", methods=["POST"])
def createStudent():
    result = utils.createStudent(request=request.json)
    if result:
        return {}, 200
    else:
        return {}, 500


@bp.route("/SQL/Lecture/create", methods=["POST"])
def createLecture():
    result = utils.createLecture(request=request.json)
    if result:
        return {}, 200
    else:
        return {}, 500


# *** READ ALL ROUTES ***
@bp.route("/SQL/Room/read_all", methods=["GET"])
def readRoom():
    response = utils.readRoom()
    if result != False:
        return {"Rooms": response}, 200
    else:
        return {}, 500


@bp.route("/SQL/Student/read_all", methods=["GET"])
def readStudent():
    response = utils.readStudent()
    if result != False:
        return {"Student": response}, 200
    else:
        return {}, 500


@bp.route("/SQL/Lecture/read_all", methods=["GET"])
def readLecture():
    response = utils.readLecture()
    if result != False:
        return {"Lecture": response}, 200
    else:
        return {}, 500


# *** UPDATE ROUTES ***
@bp.route("/SQL/Room/update/<int:id>", methods=["PUT"])
def updateRoom(id: int):
    response = utils.updateRoom(id=id, request=request.json)
    if response:
        return {}, 200
    else:
        return {}, 500


@bp.route("/SQL/Student/update/<int:id>", methods=["PUT"])
def updateStudent(id: int):
    response = utils.updateStudent(id=id, request=request.json)
    if response:
        return {}, 200
    else:
        return {}, 500


@bp.route("/SQL/Lecture/update/<int:id>", methods=["PUT"])
def updateLecture(id: int):
    response = utils.updateLecture(id=id, request=request.json)
    if response:
        return {}, 200
    else:
        return {}, 500


# *** DELETE ROUTES ***
@bp.route("/SQL/Room/delete/<int:id>", methods=["DELETE"])
def deleteRoom(id: int):
    response = utils.deleteRoom(id=id)
    if response:
        return {}, 200
    else:
        return {}, 500


@bp.route("/SQL/Student/delete/<int:id>", methods=["DELETE"])
def deleteStudent(id: int):
    response = utils.deleteStudent(id=id)
    if response:
        return {}, 200
    else:
        return {}, 500


@bp.route("/SQL/Lecture/delete/<int:id>", methods=["DELETE"])
def deleteLecture(id: int):
    response = utils.deleteLecture(id=id)
    if response:
        return {}, 200
    else:
        return {}, 500
