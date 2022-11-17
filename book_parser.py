import requests
from bs4 import BeautifulSoup

print("Process started...")
url = "https://readrate.com/rus/ratings/top100"
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
books = soup.find_all('a', class_='title-link d-inline-block')
names = soup.find_all('h4', class_='')
file = open('names.txt', 'w')
file.write("Топ 10 книг по мнению сайта ReadRate: " + '\n')
for items in names:
	name = str(items).replace('<h4>', '').replace('</h4>', '')
	file.write(name + '\n')
file.close()
print("Process successfull")
quit()