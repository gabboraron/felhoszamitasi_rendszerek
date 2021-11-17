#!/usr/bin/python
import requests
import json 
import html
import sys

requestpost = requests.post('https://awxyhe.web.elte.hu/koronavirus/fetchallnews.php')
response_data = requestpost.json()
# print(html.unescape(response_data["news"][0]))
# currentNews = json.loads(response_data["news"][0])
# print(html.unescape(currentNews["title"]))
# print(html.unescape(currentNews["description"]))
# print(html.unescape(currentNews["link"]))
# print(requestpost.status_code)

data = []
status = 0
answers = 0
out = {"data":[], "status":[], "answers":[0]}


searchterm = sys.argv[1]

error = 0

if requestpost.status_code == 200:
	out["status"] = 200
	for news in response_data["news"]:
		try:
			currentNews = json.loads(news)
			if ((html.unescape(currentNews["title"]) != "Array" and html.unescape(currentNews["title"]).lower().find(searchterm.lower()) != -1) or (html.unescape(currentNews["description"]).lower().find(searchterm.lower()) != -1)):
				# print(html.unescape(currentNews["timestamp"]))
				# print(html.unescape(currentNews["title"]))
				# print(html.unescape(currentNews["description"]))
				# print(html.unescape(currentNews["link"]))
				outnews = {html.unescape(currentNews["timestamp"]), html.unescape(currentNews["title"]), html.unescape(currentNews["description"]), html.unescape(currentNews["link"])}
				out["data"].append(outnews)
				out["answers"][0] = out["answers"][0] +1
		except:
			#print("\n --- \n")
			error += 1
else:
	out["status"] = 404
	#print("404")

print (out)