#!/usr/bin/python
import requests
import json 
import html
import sys

requestpost = requests.post('https://awxyhe.web.elte.hu/koronavirus/updatesqldb.php')
requestpost = requests.post('https://awxyhe.web.elte.hu/koronavirus/fetchallnews.php')
response_data = requestpost.json()

searchterm = sys.argv[1]

out = []

error = 0
status = 0
nrOfResults = 0

if requestpost.status_code == 200:
	status = 200
	for news in response_data["news"]:
		try:
			currentNews = json.loads(news)
			if ((html.unescape(currentNews["title"]) != "Array" and html.unescape(currentNews["title"]).lower().find(searchterm.lower()) != -1) or (html.unescape(currentNews["description"]).lower().find(searchterm.lower()) != -1)):			
				outnews = [html.unescape(currentNews["timestamp"]), html.unescape(currentNews["title"]), html.unescape(currentNews["description"]), html.unescape(currentNews["link"])]
				out.append(outnews)
				nrOfResults = nrOfResults +1
		except:
			error += 1
else:
	status = 404

out.append(status)
out.append(nrOfResults)

#outnews = [html.unescape(currentNews["timestamp"]), html.unescape(currentNews["title"]), html.unescape(currentNews["description"]), html.unescape(currentNews["link"])]
print(json.dumps(out))


#print(json.dumps(str(out).replace('"', "'")))
#print (out)