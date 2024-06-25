from db import conn, cursor


user_input = "adventure books"

read_data = "SELECT * FROM web_data"
cursor.execute(read_data)
result = cursor.fetchall()

print(result)