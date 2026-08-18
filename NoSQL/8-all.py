#!/usr/bin/env python3
"""Module 8 - Function to list all documents in a collection."""


def list_all(mongo_collection):
    """Returns all documents in a collection."""
    return list(mongo_collection.find())
