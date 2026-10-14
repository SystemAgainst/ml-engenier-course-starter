numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

"""1st way to expand the list"""
new_numbers = numbers[::-1]

"""2nd way to expand the list"""
numbers.reverse()

"""3rd way to expand the list"""
new_numbers = reversed(numbers) 
print(type(new_numbers)) # <class 'list_reverseiterator'>
new_numbers = list(reversed(numbers))
