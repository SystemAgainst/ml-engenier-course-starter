import requests

url = 'https://api.binance.com/api/v3/ticker/price'
params = {'symbol': 'BTCUSDT'}

try:
    response = requests.get(url, params)
    bitcoin_price = response.json()["price"]
    price = float(bitcoin_price)
    print(price)
except requests.exceptions.ConnectionError as error:
    print(f"Something goes wrong: {error}")