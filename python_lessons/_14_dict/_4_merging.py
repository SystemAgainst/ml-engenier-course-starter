person = {
    "city": "New York",
    "age": 30,
    "name": "John",
}
additional_person_info = {
    "job": "Engineer",
    "married": True,
    "city": "London"
}

'''если есть одинаковые свойства, то "обновляется" на значение свойства, которое было положено в update()'''
person.update(additional_person_info) 
print(person) # {'city': 'London', 'age': 30, 'name': 'John', 'job': 'Engineer', 'married': True}

'''другой способ объединения'''
person = person | additional_person_info
print(person)