fruits = ['banana', 'apple', 'cherry', 'date']
sorted_fruits = sorted(fruits)
reversed_sorted_fruits = sorted(fruits, reverse=True)
print(sorted_fruits) # ['apple', 'banana', 'cherry', 'date']
print(reversed_sorted_fruits) # ['date', 'cherry', 'banana', 'apple']
print(fruits) # первоначальный список не изменился


def sort_by_len(element: str) -> int:
  return len(element)


print(sort_by_len) # <function sort_by_len at 0x102ad23e0>
print(type(sort_by_len)) # <class 'function'>

'''
1. Сначала сработает по ключу и отсортирует по ключу sort_by_len
2. отсортирует полученный результат в порядке увеличения
'''
new_sorted_fruits = sorted(fruits, key=sort_by_len) # без скобок, нам не надо ее вызывать
print(new_sorted_fruits) # ['date', 'apple', 'banana', 'cherry']

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 30},
]


def sort_by_age(person: dict) -> int:
    return person["age"]


sorted_people = sorted(people, key=sort_by_age)
print(sorted_people) # [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 30}]

print("\n")

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Diana", "age": 30},
    {"name": "Charlie", "age": 30},
]


def sort_by_age_name(person: dict) -> tuple[int, str]:
   return person['age'], person['name']


sorted_people_by_age_and_name = sorted(people, key=sort_by_age_name)
print(sorted_people_by_age_and_name) # [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 30}, {'name': 'Diana', 'age': 30}]
