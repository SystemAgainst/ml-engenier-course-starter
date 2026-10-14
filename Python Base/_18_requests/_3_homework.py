'''
задание
1. Отправьте на https://api.binance.com/api/v3/ticker/price запрос БЕЗ аргумента params.
2. Изучите структуру ответа, сравните её с ответом в запросе без params.
3. Напишите код, который найдёт курс Etherium'а к доллару (ETHUSDT) в полученной из запроса структуре.
'''

import requests

url = 'https://api.binance.com/api/v3/ticker/price'
# params = {'symbol': 'ETHUSDT'}

response_without_params = requests.get(url)

#print(response_without_params) # <Response [200]>

for ticket in response_without_params.json():
  if ticket['symbol'] == 'ETHUSDT':
    print(ticket['price']) # 