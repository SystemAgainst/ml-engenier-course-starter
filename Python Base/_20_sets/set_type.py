my_set = {1, 2, 3, 4, 5}
print(type(my_set)) # <class 'set'>
print(my_set) # {1, 2, 3, 4, 5}

my_set_2 = set()
for i in range(5):
  my_set_2.add(i)
print(my_set_2) # {0, 1, 2, 3, 4}

my_set_remove_item = {0, 1, 3, 4, 6, 99}
my_set_remove_item.remove(99) # remove current item, not index
print(my_set_remove_item) # {0, 1, 3, 4, 6}

'''set contains only unique items'''
unique_set = {0, 1, 3, 4, 6, 99}
unique_set.add(99)
print(unique_set) # {0, 1, 3, 4, 99, 6}

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2)) # {1, 2, 3, 4, 5, 6}

united_set = set1.union(set2)
print(len(united_set)) # 6
print(set1.intersection(set2)) # {3, 4}
print(set1.difference(set2)) # {1, 2}, set 1 содержит те элементы, а именно {1, 2}, к-ая не содержит значение передаваемая в скобку difference (set2)

squares = {x**2 for x in range(5)}
print(type(squares)) # <class 'set'>
print(squares) # {0, 1, 4, 9, 16}

'''set - неупорядоченная последовательность'''
print({1, 2, 3} == {3, 2, 1}) # True

numbers = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]
unique_numbers = set(numbers)
print(type(unique_numbers)) # <class 'set'>
print(unique_numbers) # {1, 2, 3, 4, 5, 6, 7}

unique_numbers = list(unique_numbers) # ~ unique_numbers = list(set(numbers))
print(type(unique_numbers)) # <class 'list'>
print(unique_numbers) # [1, 2, 3, 4, 5, 6, 7]