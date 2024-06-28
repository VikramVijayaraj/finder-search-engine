from db_connection import connection


def create_table():
    query = """
        CREATE TABLE IF NOT EXISTS books_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            url VARCHAR(255) NOT NULL,
            title VARCHAR(255),
            metadata TEXT,
            FULLTEXT(title, metadata)
        )
        """

    cursor = connection.cursor()
    cursor.execute(query)
    print(f"Table created successfully")

    cursor.close()


if __name__ == "__main__":
    create_table()
