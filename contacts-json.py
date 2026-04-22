#!/usr/bin/env python3

import pymysql
import json

print("Content-Type: application/json\n")

conn = pymysql.connect(
    host="localhost",
    user="webuser",
    password="password123",
    database="contactsdb"
)

cursor = conn.cursor()
cursor.execute("SELECT name, phone FROM contacts")

rows = cursor.fetchall()

data = []

for row in rows:
    data.append({
        "name": row[0],
        "telephone": row[1]
    })

result = {
    "ok": True,
    "count": len(data),
    "data": data
}

print(json.dumps(result))

