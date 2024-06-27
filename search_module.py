from db import conn, cursor


def search_webpages(search_query):
    query = """
        SELECT url, title, metadata, MATCH(title, metadata) AGAINST(%s IN NATURAL LANGUAGE MODE) AS score
        FROM web_data
        WHERE MATCH(title, metadata) AGAINST(%s IN NATURAL LANGUAGE MODE)
        ORDER BY score DESC
    """

    cursor.execute(query, (search_query, search_query))
    results = cursor.fetchall()
    return results


# user_input = "five are together book"
# search_webpages(user_input)


# Close database connection
# cursor.close()
# conn.close()
