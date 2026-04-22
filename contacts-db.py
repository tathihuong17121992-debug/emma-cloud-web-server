#!/usr/bin/env python3

import pymysql

print("Content-Type: text/html\n")

conn = pymysql.connect(
    host="localhost",
    user="webuser",
    password="password123",
    database="contactsdb"
)

cursor = conn.cursor()
cursor.execute("SELECT name, phone FROM contacts")

print("""
<html>
<head>
<title>Contacts</title>
<style>
table {border-collapse: collapse;}
th, td {border:1px solid black;padding:10px;}
</style>
</head>

<body>

<h1>연락처</h1>

<table>
<tr>
<th>이름</th>
<th>전화번호</th>
</tr>
""")

for name, phone in cursor.fetchall():
    print(f"<tr><td>{name}</td><td>{phone}</td></tr>")

print("""
</table>
</body>
</html>
""")

conn.close()
