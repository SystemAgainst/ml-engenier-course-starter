name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")  # Outputs: "My name is Alice and I am 30 years old."

x = 5
y = 10
print(f"summary is {x + y}, multiplication is {x * y}")  # Output: summary is 15, multiplication is 50

my_string = input("Enter a number: ")
if my_string.isdigit():
    my_integer = int(my_string)
    print(f"You entered the integer: {my_integer}")
else:
    print(f"You did not enter a valid integer. {my_string} is not an integer.")
