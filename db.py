import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
    host="localhost",        # Replace with your host
    user="root",             # Replace with your username
    password="Vicky_2000",     # Replace with your password
    database="search_engine"        # Replace with your database name
)

# Create a cursor object
cursor = conn.cursor()

# Create table if it does not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS web_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(255) NOT NULL,
    title VARCHAR(255),
    metadata TEXT
)
""")

# Insert a single record
# sql = "INSERT INTO employees (name, age, gender) VALUES (%s, %s, %s)"
# val = ("John Doe", 28, "Male")
# cursor.execute(sql, val)

# Insert multiple records
# sql = "INSERT INTO employees (name, age, gender) VALUES (%s, %s, %s)"
# vals = [
#     ("Jane Doe", 25, "Female"),
#     ("Mike Smith", 30, "Male"),
#     ("Sara Connor", 27, "Female")
# ]
# cursor.executemany(sql, vals)

# Commit the transaction
# conn.commit()

# print(cursor.rowcount, "record(s) inserted.")

# Close the cursor and connection
# cursor.close()
# conn.close()
