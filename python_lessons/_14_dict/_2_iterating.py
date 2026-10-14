person = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

for item in person.items():
    print(item)
    key, value = item
    print(f"key: {key}, value: {value}")
    print(type(item))

print("\n")

for key, value in person.items():
  print(f"key: {key}, value: {value}")

print("\n")

for key in person.keys():
  print(f"{key}")

print("\n")

for value in person.values():
  print(f"{value}")
