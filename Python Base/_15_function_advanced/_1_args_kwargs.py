def add(x: int, y: int) -> int:
  return x + y


def add_all(*args) -> int:
  print(args) # (1, 2, 3)
  print(type(args)) # <class 'tuple'>

  summary = 0
  for num in args:
    summary += num
  return summary


print(add_all(1, 2, 3))
print(add_all(1, 2, 3, 4, 5))  # Outputs: 15


values = [1, 2, 3, 4, 5]
other_values = [6, 7, 8, 9, 10]

print(add_all(*values))  # Outputs: 15
print(add_all(*values, *other_values))  # Outputs: 55


def introduce(**kwargs):
  print(kwargs) # {}
  print(type(kwargs)) # <class 'dict'>
  print("----")
  for key, value in kwargs.items():
    print(key)
    print(value)


introduce(name="John", age=30, city="New York")

person = {
    "city": "New York",
    "age": 30,
    "name": "John",
}
introduce(**person)

print("\n")


def func_with_all_arguments(x: int, y: int, *args, value: int = 6, **kwargs):
    print(x, y)
    print(args)
    print(value)
    print(kwargs)


func_with_all_arguments(1, 2, 3, 4, 5, **person)