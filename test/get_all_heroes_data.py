import json
import requests
from bs4 import BeautifulSoup
URL = 'https://superheroapi.com/ids.html'
proxy = {'http': 'http://proxy.server:3138'}
hero_page = requests.get(URL, proxies=proxy).text
heroes_parser = BeautifulSoup(hero_page, 'html.parser')
heroes_data = {}
for row in heroes_parser.find_all('tr'):
    ids, name = row.find_all('td')[0].get_text(), row.find_all('td')[1].get_text()
    heroes_data[name] = ids
with open('heros_data.json', 'w+') as f:
    json_data = json.dumps(heroes_data)
    f.write(json_data)