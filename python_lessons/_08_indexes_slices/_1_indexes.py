fruits = ["apple", "banana", "cherry", "watermelon"]
print(fruits[0]) # apple
print(fruits[-4]) # apple
#print(fruits[4]) # IndexError: list index out of range
#print(fruits[-5]) # IndexError: list index out of range

fruits[0] = "pineapple"
print(fruits) # ['pineapple', 'banana', 'cherry', 'watermelon']

fruits[0], fruits[3] = fruits[3], fruits[0]
print(fruits) # ['watermelon', 'banana', 'cherry', 'pineapple']


