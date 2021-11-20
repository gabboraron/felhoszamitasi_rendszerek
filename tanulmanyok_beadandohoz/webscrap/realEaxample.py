from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://index.hu/').text
#print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
articles = soup.find_all('div',class_='cimlap-anyag')
for article in articles:
	print(article.h1.a.text)
