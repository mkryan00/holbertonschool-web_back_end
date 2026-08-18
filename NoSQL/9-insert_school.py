#!/usr/bin/env python3
"""Module 9 - Function to insert a new document into a collection."""


def insert_school(mongo_collection, **kwargs):
    """"Inserts a document into a collection and returns the ID."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserterd_id
