import requests
from bs4 import BeautifulSoup
from datetime import datetime


# start = datetime.now()
URL = "https://quotes.toscrape.com/"
response = requests.get(URL)

# soup = BeautifulSoup(response.text, 'html.parser')
soup = BeautifulSoup(response.text, 'lxml' )

# end = datetime.now() - start
# print(type(soup))
# print(end)

# print(soup)

# quotes = soup.find_all('span', class_="text")
# quotes = soup.find('span', id="myId", class_="text")
# quotes = soup.select("span.text")
# quotes = soup.select_one("span.text")
# print(quotes.name)
# print(quotes.text.strip())
# print(quotes.get_text(strip=True))
# print(quotes.get("itemprop"))
# quotes.decompose()
# quotes = soup.select_one("span.text")
# print(quotes.text.strip())
# quotes = soup.find('div', class_="quote")
# print(quotes.find_next_sibling())
# print(quotes.find_next_siblings())
# print(quotes.find_previous_siblings())
# print(quotes.descendants)

# for item in quotes.descendants:
#     if item.name == 'a':
#         print(item.get('href'))

quotes_list = []

quotes = soup.find_all('span', class_="text")
authors = soup.find_all('small', class_="author")
# tags = soup.find_all('div', class_="tags")

# print(quotes)

for i in range(0, len(quotes)):
    quote = {}
    quote["quote"] = quotes[i].text
    quote["author"] =  authors[i].text
    quote["author_info"] = URL + authors[i].find_next_sibling().get('href')[1:]
    # print(quotes[i].text)
    # print('--' + authors[i].text)
    # parseTags = tags[i].find_all('a', class_="tag")
    # for tag in parseTags:
    #     print(tag.text)
    # print()
    quotes_list.append(quote)

print(quotes_list)
