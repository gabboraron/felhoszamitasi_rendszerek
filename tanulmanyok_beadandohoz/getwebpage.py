#!/usr/bin/python
import requests

response = requests.get('https://index.hu/')

print(response.content)
print(response.status_code)