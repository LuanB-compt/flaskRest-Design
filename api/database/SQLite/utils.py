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
Functions to create, read, update and delete objects in SQLite from API.
"""


from ..models.SQLite import Lecture, Student, Room, db


# *** CREATE ***
def createRoom(request: dict) -> bool:
    """Function to create a new object in SQLite (Room table) from a request.

    Args:
        request (dict)

    Returns:
        True: If the creation is sucessfull.
        False: If the creation failed.
    """
    try:
        new_room = Room(
            capacity=request["capacity"],
            filled=request["filled"]
        )
        db.session.add(new_room)
        db.session.flush()
        db.session.commit()
        return True
    except Exception as e:
        print("Exception:", e)
        return False


def createStudent(request: dict) -> bool:
    """Function to create a new object in SQLite (Student table) from a request.

    Args:
        request (dict)

    Returns:
        True: If the creation is sucessfull.
        False: If the creation failed.
    """
    try:
        new_student = Student(
            name_=request["name"],
            cpf=request["cpf"],
        )
        db.session.add(new_student)
        db.session.flush()
        db.session.commit()
        return True
    except Exception as e:
        print("Exception:", e)
        return False


def createLecture(request: dict) -> bool:
    """Function to create a new object in SQLite (Lecture table) from a request.

    Args:
        request (dict)

    Returns:
        True: If the creation is sucessfull.
        False: If the creation failed.
    """
    try:
        new_lecture = Lecture(
            id_room=request["id_room"],
            id_student=request["id_student"],
        )
        db.session.add(new_lecture)
        db.session.flush()
        db.session.commit()
        return True
    except Exception as e:
        print("Exception:", e)
        return False


# *** READ ***
def readRoom() -> list[dict]:
    """Function to read all the objects in SQLite (Room table).

    Returns:
        list[dict]: list of objects from the table.
        False: If the reading failed.
    """
    try:
        return [room.to_dict() for room in Room.query.all()]
    except Exception as e:
        print("Exception:", e)
        return False


def readStudent() -> list[dict]:
    """Function to read all the objects in SQLite (Student table).

    Returns:
        list[dict]: list of objects from the table.
        False: If the reading failed.
    """
    try:
        return [stud.to_dict() for stud in Student.query.all()]
    except Exception as e:
        print("Exception:", e)
        return False


def readLecture() -> list[dict]:
    """Function to read all the objects in SQLite (Lecture table).

    Returns:
        list[dict]: list of objects from the table.
        False: If the reading failed.
    """
    try:
        return [lec.to_dict() for lec in Lecture.query.all()]
    except Exception as e:
        print("Exception:", e)
        return False


# *** UPDATE ***
def updateRoom(id: int, request: dict) -> bool:
    """Function to update a specific object in SQLite (Room table).

    Args:
        id (int): the object ID.
        request (dict): the new data to update.

    Returns:
        True: If the update was sucessfull.
        False: If the update failed.
    """
    try:
        room = db.session.query(Room).filter(Room.id == id).first()
        room.update_by_dict(new=request)
        return True
    except Exception as e:
        print("Exception:", e)
        return False


def updateStudent(id: int, request: dict) -> bool:
    """Function to update a specific object in SQLite (Student table).

    Args:
        id (int): the object ID.
        request (dict): the new data to update.

    Returns:
        True: If the update was sucessfull.
        False: If the update failed.
    """
    try:
        stud = db.session.query(Student).filter(Student.id == id).first()
        stud.update_by_dict(new=request)
        return True
    except Exception as e:
        print("Exception:", e)
        return False


def updateLecture(id: int, request: dict) -> bool:
    """Function to update a specific object in SQLite (Lecture table).

    Args:
        id (int): the object ID.
        request (dict): the new data to update.

    Returns:
        True: If the update was sucessfull.
        False: If the update failed.
    """
    try:
        lec = db.session.query(Lecture).filter(Lecture.id == id).first()
        lec.update_by_dict(new=request)
        return True
    except Exception as e:
        print("Exception:", e)
        return False


# *** DELETE ***
def deleteRoom(id: int) -> bool:
    """Function to delete a specific object in SQLite (Room table).

    Args:
        id (int): the object ID.

    Returns:
        True: If the delete was sucessfull.
        False: If the delete failed.
    """
    try:
        db.session.query(Room).filter(Room.id == id).delete()
        db.session.commit()
        return True
    except Exception as e:
        print("Exception:", e)
        return False


def deleteStudent(id: int) -> bool:
    """Function to delete a specific object in SQLite (Student table).

    Args:
        id (int): the object ID.

    Returns:
        True: If the delete was sucessfull.
        False: If the delete failed.
    """
    try:
        db.session.query(Student).filter(Student.id == id).delete()
        db.session.commit()
        return True
    except Exception as e:
        print("Exception:", e)
        return False


def deleteLecture(id: int) -> bool:
    """Function to delete a specific object in SQLite (Lecture table).

    Args:
        id (int): the object ID.

    Returns:
        True: If the delete was sucessfull.
        False: If the delete failed.
    """
    try:
        db.session.query(Lecture).filter(Lecture.id == id).delete()
        db.session.commit()
        return True
    except Exception as e:
        print("Exception:", e)
        return False
