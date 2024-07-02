from db_connection import create_connection


def search_webpages(search_query):
    connection = create_connection()
    cursor = connection.cursor()
    query = """
        SELECT url, title, metadata, MATCH(title, metadata) AGAINST(%s IN NATURAL LANGUAGE MODE) AS score
        FROM books_data
        WHERE MATCH(title, metadata) AGAINST(%s IN NATURAL LANGUAGE MODE)
        ORDER BY score DESC
    """

    cursor.execute(query, (search_query, search_query))
    results = cursor.fetchall()
    cursor.close()
    return results

