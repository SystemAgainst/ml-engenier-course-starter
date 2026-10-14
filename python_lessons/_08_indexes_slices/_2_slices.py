numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

"""getting first 4 items"""
new_numbers = numbers[0:5]
print(new_numbers) # [0, 1, 2, 3, 4]

"""getting all items"""
new_numbers = numbers[0:len(numbers)]
print(new_numbers) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

"""usage other syntaxis if we wish all items"""
new_numbers = numbers[:]
print(new_numbers) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


"""usage other syntaxis if we wish only first 5 items"""
new_numbers = numbers[:5]
print(new_numbers) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

"""slice with step x"""
new_numbers = numbers[0:len(numbers):2] # or ~ numbers[::2]
print(new_numbers) # [0, 2, 4, 6, 8]

"""reverse slice"""
new_numbers = numbers[::-1]
print(new_numbers) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

"""all operations, that we used for slice, we can use for strings"""
string = "Hello, world!"
print(string[5:]) # , world!
print(string[::2]) # Hlo ol!


