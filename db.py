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

# Add Fulltext column to the table
cursor.execute("""
    ALTER TABLE web_data
    ADD FULLTEXT(title, metadata)
""")

conn.commit()