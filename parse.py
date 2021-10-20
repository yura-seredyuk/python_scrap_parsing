import requests
from bs4 import BeautifulSoup
from datetime import datetime


URL = "http://quotes.toscrape.com/"
response = requests.get(URL)

# print(type(response.text))

soup = BeautifulSoup(response.text, 'html.parser')
# soup = BeautifulSoup(response.text, 'lxml')

# print(type(soup))

# quotes = soup.find_all('span',class_='text')
# quotes = soup.find('span', itemprop="text", class_='text')
# quotes = soup.select('span.text')
# quotes = soup.select_one('span.text')
# print(quotes)
# print(quotes.name)
# print(quotes.text.strip())
# print(quotes.get_text(strip=True))
# print(quotes.get('itemprop'))

# quotes.decompose()
# quotes = soup.select_one('span.text')
# print(quotes.text.strip())
# quotes = soup.find('div', class_="quote")
# print(quotes)
# print('NEXT:',quotes.find_next('div'))
# print('NEXT:',quotes.find_next_sibling())
# print('NEXT:',quotes.find_next_siblings())
# print('NEXT:',quotes.find_previous_sibling())
# print(quotes.descendants)

# for item in quotes.descendants:
#     if item.name == 'a':
#         print(item.get('href'))

quotes_list = []

quotes = soup.find_all('span',class_='text')
authors = soup.find_all('small',class_='author')

# print(authors)

for i in range(0, len(quotes)):
    quote = {}
    quote["quote"] = quotes[i].get_text(strip=True)
    quote["author"] = authors[i].get_text(strip=True)
    quote["author_info"] = URL + authors[i].find_next_sibling().get('href')
    quotes_list.append(quote)

print(quotes_list)