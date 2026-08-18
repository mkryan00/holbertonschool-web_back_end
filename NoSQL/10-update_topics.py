#!/usr/bin/env python3
"""
Module 10 - Function to change
all topics of a school document based on a name.
"""


def update_topics(mongo_collection, name, topics):
    """Updates all topics of a school based on the name."""
    mongo_collection.updateMany(
        {"name": name},
        {"$set": {"topics": topics}}
    )
