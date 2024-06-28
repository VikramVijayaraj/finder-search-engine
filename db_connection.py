# db_connection.py
import mysql.connector
from mysql.connector import Error
from config import DATABASE_CONFIG


def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=DATABASE_CONFIG['host'],
            user=DATABASE_CONFIG['user'],
            password=DATABASE_CONFIG['password'],
            database=DATABASE_CONFIG['database']
        )
        if connection.is_connected():
            print("Connection to MySQL DB is successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


# Create a single connection instance
connection = create_connection()
