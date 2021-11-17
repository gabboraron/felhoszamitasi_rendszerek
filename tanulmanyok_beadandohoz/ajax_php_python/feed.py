#!/usr/bin/python
import requests
import json 
import html
import sys

requestpost = requests.post('https://awxyhe.web.elte.hu/koronavirus/fetchallnews.php')
searchterm = sys.argv[1]
response_data = requestpost.json()
# print(html.unescape(response_data["news"][0]))
currentNews = json.loads(response_data["news"][0])

error = 0
answers = 0

if requestpost.status_code == 200:
	for news in response_data["news"]:
		try:
			currentNews = json.loads(news)
			if ((html.unescape(currentNews["title"]) != "Array" and html.unescape(currentNews["title"]).find(searchterm) != -1) or (html.unescape(currentNews["description"]).find(searchterm) != -1)):
				print(html.unescape(currentNews["timestamp"]))
				print(html.unescape(currentNews["title"]))
				print(html.unescape(currentNews["description"]))
				print(html.unescape(currentNews["link"]))
				answers = answers +1
		except:
			#print("\n --- \n")
			error += 1
else:
	print("404")