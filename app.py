#!/usr/bin/python3

import requests 
import json 
import logging 

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

# print(response.text) - prints the text of the responses, but only as a string even though it looks like a JSON

response = json.loads(response.text) # loading the text of the response in JSON

id = response ['id']
setup = response ['setup']
punchline = response['punchline']

print(id, setup, punchline)
