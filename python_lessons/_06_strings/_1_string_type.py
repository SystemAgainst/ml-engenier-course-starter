my_string = "Hello, world!"
my_string = 'Hello, world!'
my_string = """
Python is an incredibly versatile programming language that has rapidly gained popularity 
and recognition in the world of technology. It is known for its simplicity, readability, 
and ease of learning, making it an ideal language for beginners.
"""

first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name

length = len(full_name)
print(length)  # Output: 11
print(len(""))  # Output: 0

my_int = 42
my_converted_string = str(my_int)
print(type(my_converted_string))  # Output: <class 'str'>
print(my_converted_string)  # Output: "42"

convert_str_to_int = int("42")
print(type(convert_str_to_int))  # Output: <class 'int'>
print(convert_str_to_int)  # Output: 42

# try_convert_invalid_value_to_int = int("Hello")
# print(type(try_convert_invalid_value_to_int))  # Output: <class 'ValueError'>

my_string = input("Enter a number: ")
print(type(my_string))  # Output: <class 'str'>

my_string = int(input("Enter a number: "))
print(type(my_string))  # Output: <class 'int'>

# есть x. Нужно найти кол-во цифр в этом числе. Например, x = 12345. Кол-во цифр = 5

bit_integer = 2 ** 1000
print(len(str(bit_integer)))  # Output: 302

my_string = "Hello, world!"
print("hello" in my_string)  # Output: True
print("Hello" in my_string)  # Output: True
print("Python" in my_string)  # Output: False

