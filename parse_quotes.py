import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pprint import pprint


URL = "https://quotes.toscrape.com/"
quotes_list = []
page = 1

def getResponse(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml' )
    return soup

while True:
    soup = getResponse(f"{URL}page/{page}/")
    page += 1
    quotes = soup.find_all('span', class_="text")
    if len(quotes) == 0: break
    authors = soup.find_all('small', class_="author")
    # tags = soup.find_all('div', class_="tags")

    for i in range(0, len(quotes)):
        quote = {}
        quote["quote"] = quotes[i].text.strip()
        quote["author"] =  authors[i].text.strip()
        quote["author_info"] = URL + authors[i].find_next_sibling().get('href')[1:]
        quotes_list.append(quote)


quotes_list = sorted(quotes_list, key = lambda quotes_list: quotes_list['author'], reverse = False)
# pprint(quotes_list)

authors_list = []
for i, item in enumerate(quotes_list):
    
    if i > 0 and item["author"] == quotes_list[i-1]["author"]: continue
    # print(item["author"])
    soup = getResponse(item["author_info"])
    author = {}
    author["name"] = soup.find('h3', class_="author-title").text.strip()
    author["born"] = soup.find('span', class_="author-born-date").text.strip()
    author["location"] = soup.find('span', class_="author-born-location").text.strip()
    author["description:"] = soup.find('div', class_="author-description").text.strip()
    authors_list.append(author)

pprint(authors_list[0])


# Зберегти всю отриману інформацію у JSON файл
#  поля словника:
    #  ім'я письменника
    #  дата народження
    #  місце народження
    #  опис
    #  список з цитатами
    #  url про автора 

# {
#     authors[
#         {
#             "author": 1,
#             "date": 1,
#             "location": 1,
#             "description": 1,
#             "quptes": [],
#             "url": 1
#         }, 
#         {
#             "author": 1,
#             "date": 1,
#             "location": 1,
#             "description": 1,
#             "quptes": [],
#             "url": 1
#         }
#     ]
# }

