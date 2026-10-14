numbers_1 = [1, 2, 3, 4, 5]
average_1 = sum(numbers_1) / len(numbers_1)
#print(average_1)  # Outputs: 3.0

numbers_2 = [6, 7, 8, 9, 10]
average_2 = sum(numbers_2) / len(numbers_2)
#print(average_2)  # Outputs: 8.0


def find_average(numbers):
  average = sum(numbers) / len(numbers)
  return average


average_1 = find_average(numbers_1)
average_2 = find_average(numbers_2)
print(average_1, average_2)


def count_volumes(string):
  VOWELS = "aeiouAEIOU"
  count = 0

  for char in string:
    if char in VOWELS:
      count += 1

  return count


print(count_volumes("hello, world!"))
print(count_volumes("Python is a very powerful language."))


def do_nothing():
  pass


do_nothing()

"""типизация здесь нужна для того, чтобы разработчик не перепутал местами аргументы"""


def formate_date(day: int, month: str) -> str:
  return f"The date is {day} of {month}"


formate_date("January", 1) # expected type 'int', got 'str' instead

print(formate_date(day=15, month="October"))

"""при создании функции, можно поставить перед параметрами *, чтобы DEVELOPER при вызове явно прописывал аргументы, как на строке 50"""


def formate_date2(*, day: int, month: str):
  return f"The date is {day} of {month}"


#print(formate_date2(15, "October")) # formate_date2() takes 0 positional arguments but 2 were given
print(formate_date2(day=15, month="October"))


def custom_greeting(*, name: str, greeting: str = "Hello") -> str:
  return f"{greeting}, {name}"

print(custom_greeting(name="John", greeting="Good morning"))
print(custom_greeting(name="John"))