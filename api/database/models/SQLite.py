# Copyright 2023-present BRAIN, IP-Facens.
#
# This project has no License, which means that this work is under
# exclusive copyright by default. More details in:
#
# https://choosealicense.com/no-permission/
#
# SCHEDULE PROBLEM:
# Timetabling problems are specific types of scheduling problems
# that deal with the assignment of certain events to time slots.
# This assignment is subject to certain hard constraints that must
# be satisfied to obtain a feasible schedule, and soft constraints
# that must be satisfied as much as possible while forming a feasible
# schedule.
#
# AUTHORS:
# Felipe Pires dos Santos, Luan Bruno Domingues de Oliveira

"""
SQLAlchemy instantiation and physical modeling of the database entities.
"""


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Room(db.Model):
    """Class to represent a Room.

    Attributes:
        id (dict): ID.
        capacity (int): maximum number os students who can take the subject.
        filled (int): quantity of students in the room.

    Methods:
        to_dict(): Method to transform the object in a dictionary.
        update_by_dict(new: dict): Method to update the object with a dictionary.
    """

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    filled = db.Column(db.Integer, default=0)

    def to_dict(self):
        """Method to transform the object in a dictionary.

        Returns:
            dict: the object transformed in dictionary.
        """
        return {
            "id": self.id,
            "capacity": self.capacity,
            "filled": self.filled
        }

    def update_by_dict(self, new: dict):
        """Method to update the object with a dictionary.

        Args:
            new (dict): _description_
        """
        self.id = new["id"]
        self.capacity = new["capacity"]
        self.filled = new["filled"]
        db.session.commit()


class Student(db.Model):
    """Class to represent a Professor.

    Attributes:
        id (dict): ID.
        name (str): the name of professor.
        cpf (str): students CPF.

    Methods:
        to_dict(): Method to transform the object in a dictionary.
        update_by_dict(new: dict): Method to update the object with a dictionary.
    """

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name_ = db.Column(db.String(20), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)

    def to_dict(self):
        """Method to transform the object in a dictionary.

        Returns:
            dict: the object transformed in dictionary.
        """
        return {
            "id": self.id,
            "name": self.name_,
            "cpf": self.cpf,
        }

    def update_by_dict(self, new: dict):
        """Method to update the object with a dictionary.

        Args:
            new (dict): _description_
        """
        self.id = new["id"]
        self.name = new["name"]
        self.cpf = new["cpf"]
        db.session.commit()


class Lecture(db.Model):
    """Class to represent a Lecture.

    Attributes:
        id (int): ID.
        id_room (int): ID of the room.
        id_student (int): ID of the student.

    Methods:
        to_dict(): Method to transform the object in a dictionary.
        update_by_dict(new: dict): Method to update the object with a dictionary.
    """

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    id_room = db.Column(
        db.Integer, db.ForeignKey("room.id"), unique=True, nullable=False
    )
    id_student = db.Column(
        db.Integer, db.ForeignKey("student.id"), unique=True, nullable=False
    )

    def to_dict(self):
        """Method to transform the object in a dictionary.

        Returns:
            dict: the object transformed in dictionary.
        """
        return {
            "id": self.id,
            "id_room": self.id_room,
            "id_student": self.id_student,
        }

    def update_by_dict(self, new: dict):
        """Method to update the object with a dictionary.

        Args:
            new (dict): _description_
        """
        self.id = new["id"]
        self.id_room = new["id_room"]
        self.id_student = new["id_student"]
        db.session.commit()
