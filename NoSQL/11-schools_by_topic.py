#!/usr/bin/env python3
"""
Module 11 - Function to return,
a list of schools having a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """Returns a list of schools by a specific topic."""
    return mongo_collection.find({"topics": topic})
