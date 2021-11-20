from bs4 import BeautifulSoup
import requests
import sys
import colorama
from colorama import Fore

pageNr = 1
nrOfArticlesAll = 0

out = []

searchterm = ''
for param in sys.argv:
	searchterm +="%20"+str(param)

while True :
	target = 'https://data.europa.eu/api/hub/search/en/feeds/datasets.rss?q=' + sys.argv[1] + '&facets={"country":[],"catalog":[],"categories":["HEAL"],"keywords":[],"scoring":[],"format":[],"license":[]}&page='+ str(pageNr) +'&limit=15&facetOperator=AND&facetGroupOperator=AND&sort=relevance+desc, modified+desc, title.en+asc'
	html_text = requests.get(target).text
	#print(html_text)
	print("loading")
	soup = BeautifulSoup(html_text, 'lxml')
	articles = soup.find_all('item')

	if len(articles) == 0:
		break

	articleObj = []

	nrOfArticlesOnThisPage = 0
	for article in articles:
		print (Fore.YELLOW + str(nrOfArticlesAll)+ ' : ' +str(nrOfArticlesOnThisPage))
		print(Fore.RED + str(article.title.text))
		#print(Fore.BLUE  + article.guid.text)
		#print(Fore.WHITE + str(article.description.text))
		#print(Fore.WHITE +str(article))
		nrOfArticlesOnThisPage += 1
		nrOfArticlesAll += 1
		articleObj.append(article.title.text)	
	pageNr += 1