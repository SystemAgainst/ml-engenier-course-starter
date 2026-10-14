person = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

print(person) # {'name': 'John', 'age': 30, 'city': 'New York'}

person["job"] = "Engineer"

print(person) # {'name': 'John', 'age': 30, 'city': 'New York', 'job': 'Engineer'}

'''2nd way declaration of dict'''
person2 = {}
person2["name"] = "John"
person2["age"] = 30
person2["city"] = "New York"
print(person2) # {'name': 'John', 'age': 30, 'city': 'New York'}

'''getting value by key'''
print(person["name"]) # Outputs: John
'''
print(person["country"]) # KeyError: 'country'

to avoid error that was demonstrated upper (string 23), use .get()
'''
print(person.get("name")) # Outputs: John
print(person.get("country")) # Outputs: None

'''we can set up default value, if we don't find the key'''
print(person.get("country", "USA")) # Outputs: USA
print(person.get("name", "Jack")) # Outputs: John


