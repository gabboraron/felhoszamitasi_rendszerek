#!/usr/bin/python
import requests
import json 
import html
import sys

requestpost = requests.post('https://www.google.com')
if requestpost.status_code == 200:
    print('OK')
else:
    print('not OK')