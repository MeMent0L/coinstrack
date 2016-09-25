#!/usr/bin/python

import sys
import urllib2
import json
import datetime

def get_position(json):
    try:
        return int(json['position'])
    except KeyError:
        return 10000

import database

db = database.coinstrack()


count = 757
created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
currency1 = "usd"
currency2 = "btc"
url = "http://coinmarketcap.northpole.ro/api/v5/all.json"
headers = ["POSITION","NAME","TICKER","CATEGORY","AVAILABLE_SUPPLY","MARKETCAP_USD","MARKETCAP_BTC","PRICE_USD","PRICE_BTC","VOLUME24_USD","VOLUME24_BTC","CHANGE1H_USD","CHANGE1H_BTC","CHANGE7H_USD","CHANGE7H_BTC","CHANGE7D_USD","CHANGE7D_BTC","TIME_CMC","TIME_COMPUTER"]

if len(sys.argv) == 2:
        count = int(sys.argv[1])


data = urllib2.urlopen(url).read()
data = json.loads(data)['markets']
data.sort(key=get_position)
btc_price = float(data[0]['price'][currency1])

table = []
text_output = []

for d in data[0:count]:
    try:
        volume_usd = float(d['volume24']['btc'])*btc_price
        volume_btc = float(d['volume24']['btc'])
    except:
        volume_usd=0
        volume_btc=0

    position=d['position']
    name=d['name'] 
    symbol=d['symbol']
    category=d['category']
    availableSupply=d['availableSupply']
    marketCap_usd=d['marketCap'][currency1]
    marketCap_btc=d['marketCap'][currency2]
    price_usd=d['price'][currency1]
    price_btc=d['price'][currency2]
    volume_usd=volume_usd
    volume_btc=volume_btc
    change1h_usd=d['change1h'][currency1]
    change1h_btc=d['change1h'][currency2]
    change7h_usd=d['change7h'][currency1]
    change7h_btc=d['change7h'][currency2]
    change7d_usd=d['change7d'][currency1]
    change7d_btc=d['change7d'][currency2]
    timestamp=d['timestamp']

    print "Inserting...", d['symbol']

    db.insert(position, name, symbol, category, availableSupply, marketCap_usd, marketCap_btc, price_usd, price_btc, volume_usd, volume_btc, change1h_usd, change1h_btc, change7h_usd, change7h_btc, change7d_usd, change7d_btc, timestamp, created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

print "Done"
