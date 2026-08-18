#!/usr/bin/env python3
"""
Module 12 - Script that provides stats
about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
db = client.logs
nginx = db.nginx

total = nginx.count_documents({})
print(f"{total} logs")

print("Methods:")
for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
    count = nginx.count_documents({"method": method})
    print(f"\t{method}: {count}")

status = nginx.count_documents({"method": "GET", "path": "/status"})
print(f"{status} status check")
