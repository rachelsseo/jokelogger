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

# print(id, setup, punchline)

logging = logging.getLogger(__name__)
logging = basicConfig(filename='joke.log', encoding='utf-8', level=logging.DEBUG) 
# logging to this filname, encode in this language, use DEBUG when logging to make it verbose
logging.warning('%s:%s:%s', id, setup, punchline) 
# in each %s, there will either be an id, setup, or punchline

