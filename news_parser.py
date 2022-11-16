import requests
from bs4 import BeautifulSoup

url = "https://www.pravda.com.ua/rus/news/"
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
newsList = soup.find('div', class_='container_sub_news_list_wrapper mode1')
news = newsList.find_all('a', class_='')
file = open('names.txt', 'w')
for items in news:
	print(items)
	file.write(str(items) + '\n')
file.close()
input()