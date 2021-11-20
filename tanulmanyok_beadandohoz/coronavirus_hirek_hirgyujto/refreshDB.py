#!/usr/bin/python
import requests

requestpost = requests.post('https://awxyhe.web.elte.hu/koronavirus/updatesqldb.php')

if requestpost.status_code == 200:
	print("refreshed")