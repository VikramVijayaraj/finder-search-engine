from bs4 import BeautifulSoup
import requests


# url = "https://www.bookswagon.com/book/doglapan-ashneer-grover/9780670097111"
url = "https://www.bookswagon.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)
meta_tags = soup.find_all('meta')
for meta in meta_tags:
    data = meta.get("name")
    if data and "description" in data.lower():
        print(meta.get("name"))
        print(meta.get("content"))
        break
# if meta_tag:
#     content = meta_tag.get('content').strip()
#     print(content)

a_tags = soup.find_all('a')
for tag in a_tags:
    link = tag.get("href")
    if link:
        print(link[:2])
# for tag in a_tags:
#     print(tag.get("href"))