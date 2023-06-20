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
Functions to create, read, update and delete objects in MongoDB from API.
"""


from bson.objectid import ObjectId

from ..models.MongoDB import mongo_client


def create_dict_from_query(doc) -> dict:
    """Function to create a dictionary from a inputed query.

    Args:
        doc: the query input.

    Returns:
        dict: the dictionary output.
    """
    json = {}
    for column in doc.keys():
        if column == "_id":
            json["id"] = str(doc[column])
        else:
            json[column] = doc[column]
    return json


def create(request: dict):
    """Function to create a new document in MongoDB from a request.

    Args:
        request (dict)

    Returns:
        dict: Empty dictionary if the creation is a sucessfull.
        None: if the creation failed.
    """
    try:
        mongo_client.db.todos.insert_one(document=request)
        return {}
    except Exception as e:
        print("Exception:", e)
        return None


def read_all() -> dict:
    """Function to read all the documents in MongoDB.

    Args:
        None.

    Returns:
        dict: dictionary with the documents.
        None: if the reading failed.
    """
    try:
        docs, response = mongo_client.db.todos.find(), {}
        for doc in docs:
            response[str(doc["_id"])] = {}
            for column in doc.keys():
                if column != "_id":
                    response[str(doc["_id"])][column] = doc[column]
        return response
    except Exception as e:
        print("Exception:", e)
        return None


def read(id: str) -> dict:
    """Function to read a specific document in MongoDB.

    Args:
        id (str): the document ID.

    Returns:
        dict: the document.
        None: if the reading failed.
    """
    try:
        doc = mongo_client.db.todos.find_one(filter={"_id": ObjectId(id)})
        return create_dict_from_query(doc=doc)
    except Exception as e:
        print("Exception:", e)
        return None


def update(id: str, request: dict) -> dict:
    """Function to update a specific document in MongoDB.

    Args:
        id (str): the document ID.
        request (dict): the new data to update.

    Returns:
        dict: the document.
        None: if the reading failed.
    """
    try:
        doc = mongo_client.db.todos.find_one_and_replace(
            filter={"_id": ObjectId(id)}, replacement=request
        )
        return create_dict_from_query(doc=doc)
    except Exception as e:
        print("Exception:", e)
        return None


def delete(id: str):
    """Function to delete a specific document in MongoDB.

    Args:
        id (str): the document ID.

    Returns:
        dict: the document.
        None: if the reading failed.
    """
    try:
        doc = mongo_client.db.todos.find_one_and_delete(filter={"_id": ObjectId(id)})
        if doc is not None:
            return create_dict_from_query(doc=doc)
        else:
            return None
    except Exception as e:
        print("Exception:", e)
        return None
