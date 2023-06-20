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
Client instancing for MongoDB management.
"""

from flask_pymongo import PyMongo

mongo_client = PyMongo()
