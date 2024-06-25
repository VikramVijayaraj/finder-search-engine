from db import conn, cursor


def search_webpages(search_query):
    query = """
        SELECT url, title, metadata, MATCH(title, metadata) AGAINST(%s IN NATURAL LANGUAGE MODE) AS score
        FROM web_data
        WHERE MATCH(title, metadata) AGAINST(%s IN NATURAL LANGUAGE MODE)
        ORDER BY score DESC
    """

    cursor.execute(query, (search_query, search_query))
    result = cursor.fetchall()

    for row in result:
        print(row[0])


user_input = "five are together book"
search_webpages(user_input)


# Close MySql connection
cursor.close()
conn.close()