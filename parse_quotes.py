import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pprint import pprint


BASE_URL = "http://quotes.toscrape.com/"
quotes_list = []
page = 1


def getSoup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

while True:
    soup = getSoup(f'{BASE_URL}page/{page}/')
    page +=1
    quotes = soup.find_all('span',class_='text')
    if len(quotes) == 0: break
    authors = soup.find_all('small',class_='author')
    for i in range(0, len(quotes)):
        quote = {}
        quote["quote"] = quotes[i].get_text(strip=True)
        quote["author"] = authors[i].get_text(strip=True)
        quote["author_info"] = BASE_URL + authors[i].find_next_sibling().get('href')
        tags = []
        tag_block = quotes[i].find_next_sibling('div', class_='tags').find_all('a')
        for item in tag_block:
            tag = {}
            tag['name'] = item.get_text(strip=True)
            tag['link'] = BASE_URL + item.get('href')
            tags.append(tag)
        quote["tags"] = tags
        quotes_list.append(quote)
    break

quotes_list = sorted(quotes_list, key = lambda quotes_list: quotes_list['author'], reverse=False)

# pprint(quotes_list)

authors_list = []
for i, item in enumerate(quotes_list):
    if i > 0 and item["author"] == quotes_list[i-1]["author"]:continue   
    # print(i, item["author"])
    soup = getSoup(item['author_info'])
    author = {}
    author["name"] = item["author"]
    author["quotes"] = []
    author["url"] = item["author_info"]
    author["date"] = soup.find('span',class_='author-born-date').get_text(strip=True)
    author["location"] = soup.find('span',class_='author-born-location').get_text(strip=True)
    author["description"] = soup.find('div',class_='author-description').get_text(strip=True)    
    authors_list.append(author)

data = {}
data["authors"] = authors_list

for quote in quotes_list:
    # print(quote["author"])
    for author in data["authors"]:
        if quote["author"] == author["name"]:

            author["quotes"].append(quote)
            break


pprint(data["authors"][0])



# {
#     "authors": [
#         {
#             "author":1,
#             "date":1,
#             "location":1,
#             "description":1,
#             "quotes":[
#                 {
#                     "text":1,
#                     "tags": [
#                         {
#                             "name":1,
#                             "link":1
#                         },
#                     ]
#                 },
#             ],
#             "url":1
#         },
#     ]
# }

