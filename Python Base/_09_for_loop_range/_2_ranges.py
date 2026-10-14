range_object = range(10)
print(range_object) # range(0, 10)

numbers = list(range_object)
print(numbers) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

my_range = range(1, 10)
print(list(my_range)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""(начало_элемента, предпоследний эл, шаг )"""
my_range = range(1, 10, 2)
print(list(my_range)) # [1, 3, 5, 7, 9]

my_range = range(10, 1, -1)
print(list(my_range)) # [10, 9, 8, 7, 6, 5, 4, 3, 2]

numbers = [10, 11, 12, 13, 14, 15]
for num in numbers:
  num += 1
print(numbers) # [10, 11, 12, 13, 14, 15], не сработало, т.к. Int (в списке) не изменяемый тип

print("\n")

for i in range(len(numbers)):
  numbers[i] += 1
print(numbers)

print("\n")

greeting = 'Hello, World!'
indexes = []
count = 0

for i in range(len(greeting)):
  if greeting[i] == "o":
    count += 1
    indexes.append(i)
print(f"count: {count} and indexes: {indexes}")
