from bs4 import BeautifulSoup
import requests
import sys
import colorama
from colorama import Fore
import urllib.request

pageNr = 1
nrOfArticlesAll = 0

out = []

searchterm = ''
for param in sys.argv:
	searchterm +=str(param)+"%20"

while True :
	url = 'https://data.europa.eu/data/datasets?categories=heal&page='+str(pageNr)+'&locale=en&query=' + searchterm
	try:
		with urllib.request.urlopen(url) as response:
			html_text = response.read().decode('utf-8') #use whatever encoding as per the webpage
	except urllib.request.HTTPError as e:
	    if e.code==404:
	        print(f"{url} is not found")
	    elif e.code==503:
	        print(f'{url} base webservices are not available')
	        ## can add authentication here 
	    else:
	        print('http error',e)


	
	#html_text = requests.get(target).text
	print(html_text)
	soup = BeautifulSoup(html_text, 'lxml')
	articles = soup.find_all('div',class_='dataset')
	print('\n\n\n\n')
	print(articles)

	if len(articles) == 0:
		break

	articleObj = []

	nrOfArticlesOnThisPage = 0
	for article in articles:
		print (Fore.YELLOW + str(nrOfArticlesAll)+ ' : ' +str(nrOfArticlesOnThisPage))
		print(Fore.RED + str(article.h2.span.text))
		#print(Fore.BLUE  + article.guid.text)
		#print(Fore.WHITE + str(article.description.text))
		#print(Fore.WHITE +str(article))
		nrOfArticlesOnThisPage += 1
		nrOfArticlesAll += 1
		#articleObj.append(article.title.text)	
	pageNr += 1