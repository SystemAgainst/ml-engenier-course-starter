person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
other_person = {
    "city": "New York",
    "age": 30,
    "name": "John",
}

other_person2 = {
    "city": "Texas",
    "age": 30,
    "name": "John",
}

other_person3 = {
    "city": "Texas",
    "age": 30,
    "name": "John",
    "surname": "Scorfild"
}

print(person == other_person)  # Outputs: True
print(person == other_person2)  # Outputs: False
print(person == other_person3)  # Outputs: False
