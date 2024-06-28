from db_connection import connection


def search_webpages(search_query):
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


# user_input = "five are together book"
# search_webpages(user_input)


# Close database connection
# cursor.close()
# conn.close()
