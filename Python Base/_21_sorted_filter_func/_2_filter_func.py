def is_even(n: int) -> bool:
    return n % 2 == 0


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered_numbers = filter(is_even, numbers)
print(type(filtered_numbers)) # <class 'filter'>
print(filtered_numbers) # <filter object at 0x104fb9d20>
print(list(filtered_numbers)) # [2, 4, 6, 8]

people = [
    {"name": "Alice", "age": 17},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 19},
    {"name": "David", "age": 40}
]


def is_adult(person: dict) -> bool:
    return person['age'] >= 18


filtered_people = list(filter(is_adult, people))
print(filtered_people) # [{'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 19}, {'name': 'David', 'age': 40}]