#!/usr/bin/python
import requests

url = 'https://academictorrents.com/database.xml'
r = requests.get(url, allow_redirects=True)

open('academictorrents_database.xml', 'wb').write(r.content)