from bs4 import BeautifulSoup
import requests
from db_connection import connection


def get_soup(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        return soup
    else:
        print(f"ERROR: Status Code {response.status_code}")
    return None


def scrape_data(url):
    soup = get_soup(url)
    content = ""
    print(url)
    if not soup:
        return

    title = str(soup.title.text).strip()
    meta_tags = soup.find_all('meta')
    for meta in meta_tags:
        data = meta.get("name")
        if data and "description" in data.lower():
            content = meta.get("content")
            break

    # Add to the dictionary
    map[url] = [title, content]


def insert_data(url, title, metadata):
    cursor = connection.cursor()
    sql = "INSERT INTO books_data (url, title, metadata) VALUES (%s, %s, %s)"
    val = (url, title, metadata)
    cursor.execute(sql, val)
    connection.commit()
    cursor.close()


# ------ Main ------
# url_list = ["https://kitabay.com/","https://www.bookswagon.com/"]
domain = input("Enter domain: ")
base_url = input("Enter Base URL: ")
map = {}

soup = get_soup(base_url)
if soup:
    scrape_data(base_url)
    a_tags = soup.find_all('a')

    for tag in a_tags:
        link = tag.get('href')
        if link:
            if link[:len(domain)] == domain:
                scrape_data(link)
            elif link[0] == "/":
                full_link = base_url + link[1:]
                scrape_data(full_link)
        print(f"Total records: {len(map)}")

    for key, values in map.items():
        insert_data(key, values[0], values[1])

# Close the connection
connection.close()