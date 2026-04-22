#!/usr/bin/env python3

print("Content-Type: text/html\n")

print("""
<html>
<head>
<title>Contacts</title>
<style>
table {
    border-collapse: collapse;
}
th, td {
    border: 1px solid black;
    padding: 10px;
}
</style>
</head>

<body>

<h1>연락처</h1>

<table>
<tr>
<th>Name</th>
<th>Phone Number</th>
</tr>
""")

with open("/var/www/cgi-bin/contacts.txt") as f:
    for line in f:
        name, phone = line.strip().split(":")
        print(f"<tr><td>{name}</td><td>{phone}</td></tr>")

print("""
</table>
</body>
</html>
""")
