#!/usr/bin/python
import requests
import os.path, time
import datetime
import xml.etree.ElementTree as ET
import sys

today = datetime.datetime.today()
modified_date = datetime.datetime.fromtimestamp(os.path.getmtime('academictorrents_database.xml'))
duration = today - modified_date
if duration.days > 30: 
	os.remove('academictorrents_database.xml') 

	url = 'https://academictorrents.com/database.xml'
	r = requests.get(url, allow_redirects=True)
	open('academictorrents_database.xml', 'wb').write(r.content)

tree = ET.parse('academictorrents_database.xml')
root = tree.getroot()


searchterm = sys.argv[1]
out = {"data":[], "status":[200], "answers":[0]}


for channel in root:
	for item in channel:
		tmp = []
		match = 0
		for child in item:
			tmp.append(child.text)			
			if (child.text.lower().find(searchterm.lower()) != -1):
				#print(child.tag, child.attrib, child.text)
				#print(child.text.find(searchterm))
				#print(item.t)
				#torrents = {}
				out["answers"][0] = out["answers"][0] +1	
				match = 1
		if match == 1:
			out["data"].append(tmp)
print(out)