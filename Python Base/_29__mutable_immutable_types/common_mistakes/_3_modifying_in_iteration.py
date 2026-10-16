'''
Правило такое: не производить модификации в коллекции итерируемых данных
'''

# bad
'''
for num in lst:
    lst.append(num ** 2)
    print(num) # ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
'''

# ok
lst = [2, 3, 4]
another_list = [i ** 2 for i in lst]
lst.extend(another_list)
print(lst)  # [2, 3, 4, 4, 9, 16]

'''почему в выводе осталась 8?'''
# bad
numbers = [1, 3, 5, 4, 8, 6]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)

print(numbers)  # output [1, 3, 5, 8]

# ok
numbers = [1, 3, 5, 4, 8, 6]
odd_numbers = []

for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)
print(odd_numbers)  # output [1, 3, 5]
