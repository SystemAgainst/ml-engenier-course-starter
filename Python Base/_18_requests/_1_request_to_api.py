import requests


url = 'https://api.binance.com/api/v3/ticker/price'

response = requests.get(url, params={'symbol': 'BTCUSDT'})

content = response.content

print(content) # b'{"symbol":"BTCUSDT","price":"83277.33000000"}'
print(type(content)) # <class 'bytes'>

price_object = response.json()
print(type(price_object)) # <class 'dict'>
print(price_object) # {'symbol': 'BTCUSDT', 'price': '83208.61000000'}

price = float(price_object["price"])
print(type(price)) # <class 'float'>
print(price) # 83230.97
