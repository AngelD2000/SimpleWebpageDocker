#!/usr/bin/python3
import MySQLdb
import cgi
import socket
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<h1> Cloud Tech</h1>")
print("<p> Testing db connection </p>")
conn = MySQLdb.connect(socket.gethostbyname('db'), "user", "my_pass", "db_test")
cursor = conn.cursor()
sql = "SELECT * FROM test"
cursor.execute(sql)
data = cursor.fetchone()
print("Message:", data[0])
print("</body>")
print("</html>")