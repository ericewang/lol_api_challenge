import requests
from pymongo import MongoClient
db = MongoClient('mongodb://localhost:27017').league

r = requests.get('https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion?champData=all&api_key=e5e33706-a57a-45bd-bc70-6d7d22196bc1').json()['data']
for champion_name, data in r.items():
    post = db.champions.update(
        {'name': champion_name},
        {'name': champion_name, 
         'data': data,
        },
        upsert=True)

r = requests.get('https://global.api.pvp.net/api/lol/static-data/na/v1.2/item?itemListData=all&api_key=e5e33706-a57a-45bd-bc70-6d7d22196bc1').json()['data']
for item_name, data in r.items():
    post = db.items.update(
        {'name': item_name},
        {'name': item_name, 
         'data': data,
        },
        upsert=True)

