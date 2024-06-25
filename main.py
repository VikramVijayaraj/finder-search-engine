from bs4 import BeautifulSoup
import requests
from db import conn, cursor


def scrape_data(url):
    res = requests.get(url)
    content = ""

    if res.status_code != 200:
        print(f"ERROR: {res.status_code}")
        return

    soup_ = BeautifulSoup(res.text, 'html.parser')
    title = str(soup_.title.text).strip()
    meta_tag = soup_.find('meta', attrs={'name': 'description'})

    if meta_tag:
        content = meta_tag.get('content').strip()

    map[url] = [title, content]


def insert_data(url, title, metadata):
    sql = "INSERT INTO web_data (url, title, metadata) VALUES (%s, %s, %s)"
    val = (url, title, metadata)
    cursor.execute(sql, val)


# ------ Main ------
base_url = "https://kitabay.com/"
map = {}
scrape_data(base_url)

response = requests.get(base_url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    a_tags = soup.find_all('a')

    for tag in a_tags:
        link = tag.get('href')
        if link[:len(base_url)] == base_url:
            scrape_data(link)
        elif link[0] == "/":
            full_link = base_url + link[1:]
            scrape_data(full_link)

    for key, values in map.items():
        insert_data(key, values[0], values[1])

    print(f"Total records: {len(map)}")
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()
