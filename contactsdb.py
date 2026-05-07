#!/usr/bin/env python3

import pymysql

# connect DB
conn = pymysql.connect(
    host="localhost",
    user="webuser",
    password="password123",
    database="contactsdb"
)

cursor = conn.cursor()
cursor.execute("SELECT name, phone, email, address, age FROM contacts")
rows = cursor.fetchall()

# ===== PHẦN HIỂN THỊ (mới) =====
print("Content-type: text/html")
print()

print("""
<html>
<head>
    <title>Contact List</title>
    <style>
        body { font-family: Arial; }
        table { border-collapse: collapse; width: 60%; }
        th, td { border: 1px solid black; padding: 8px; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>Contact List</h1>

    <table>
        <tr>
            <th>Name</th>
            <th>Phone</th>
            <th>Email</th>
            <th>Address</th>
            <th>Age</th>
""")

for row in rows:
    name, phone, email, address, age = row
    print(f"""
        <tr>
            <td>{name}</td>
            <td>{phone}</td>
            <td>{email}</td>
            <td>{address}</td>
            <td>{age}</td>
        </tr>
    """)

print("""
    </table>
</body>
</html>
""")

conn.close()
