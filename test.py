from bs4 import BeautifulSoup
import requests
from db import conn, cursor


def add_data(url):
    new_content = ""
    new_response = requests.get(url)
    new_soup = BeautifulSoup(new_response.text, 'html.parser')
    new_title = str(new_soup.title.text).strip()
    new_meta_tag = new_soup.find('meta', attrs={'name': 'description'})
    if new_meta_tag:
        new_content = new_meta_tag.get('content').strip()

    map[url] = [new_title, new_content]

    new_sql = "INSERT INTO web_data (url, title, metadata) VALUES (%s, %s, %s)"
    new_val = (url, new_title, new_content)
    cursor.execute(new_sql, new_val)
    conn.commit()


# ------ Main ------
base_url = "https://kitabay.com/"
map = {}
all_urls = []

response = requests.get(base_url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    title = str(soup.title.text).strip()
    meta_tag = soup.find('meta', attrs={'name': 'description'})
    content = meta_tag.get('content').strip()

    map[base_url] = [title, content]

    # sql = "INSERT INTO web_data (url, title, metadata) VALUES (%s, %s, %s)"
    # val = (base_url, title, content)
    # cursor.execute(sql, val)

    a_tags = soup.find_all('a')
    i = 0  # for testing
    for tag in a_tags:
        link = tag.get('href')

        if link[:len(base_url)] == base_url:
            add_data(link)
        elif link[0] == "/":
            new_link = base_url + link[1:]
            add_data(new_link)

        # for testing
        if i == 3: break
        i += 1

print(map)
# print(cursor.rowcount, "record(s) inserted.")
#
# # Close the cursor and connection
# cursor.close()
# conn.close()
