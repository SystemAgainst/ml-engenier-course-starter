fruits = ['apple', 'banana', 'cherry']
print(fruits) # ['apple', 'banana', 'cherry']
print(len(fruits)) # 3

print("banana" in fruits) # True
print("watermelon" in fruits) # False

my_list = ["apple", 1, 1.5, True, [1, 2, 3]]
print(my_list) # ['apple', 1, 1.5, True, [1, 2, 3]]

my_list1 = [1, 2, 3]
my_list2 = [1, 3, 2]
my_list3 = [1, 2, 3]

print(my_list1 == my_list2) # False
print(my_list1 == my_list3) # True

print(bool([])) # False
print(bool([0])) # True

element1 = "apple"
element2 = "banana"
element3 = "cherry"
fruits2 = [element1, element2, element3]
print(fruits2) # ['apple', 'banana', 'cherry']

word = "hello"
my_list = list(word)
print(my_list) # ['h', 'e', 'l', 'l', 'o']

my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]
my_list3 = my_list1 + my_list2
print(f"my_list3: {my_list3}") # my_list3: [1, 2, 3, 4, 5, 6]

fruits.append("watermelon")
print(f"fruits is appended with watermelon: {fruits}") # fruits is appended with watermelon: ['apple', 'banana', 'cherry', 'watermelon']

my_string = "hello, world"
new_string = my_string.replace("world", "python")
print(f"my_string: {my_string} /n new_string: {new_string}") # 
