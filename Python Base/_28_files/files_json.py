import json


data = {"name": "Mike", "age": 30, "city": "New York"}

file = open("files/data.json", "w") 

json.dump(data, file, indent=4)

file.close() # если не закрыть -> произойдет утечка памяти. Что такое утечка памяти, приведи популярный пример, как это отразиться, как это выглядит и чем чревато?


file = open('files/data.json', 'r')
loaded_data = json.load(file)
print(loaded_data)
file.close()