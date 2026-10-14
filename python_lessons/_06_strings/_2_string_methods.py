my_string = 'Alice'
print(my_string.upper())  # Outputs: 'ALICE'

my_string = 'ALICE'
print(my_string.lower())  # Outputs: 'alice'

my_string = '    Hello, world!    '
print(len(my_string))  # Outputs: 21
print(len(my_string.strip()))  # Outputs: 13
print(f"strip: my_string.strip(): {my_string.strip()}")  # Outputs: 'Hello, world!'

my_string = 'Hello, world!'
print(f"replace: my_string.replace('world', 'Python'): {my_string.replace('world', 'Python')}")  # Outputs: 'Hello, Python!'

my_string = 'Hello, world!'
print(f"count (чтобы определить кол-во символов): my_string.count('l'): {my_string.count('l')}")  # Outputs: 3
print(f"count (чтобы определить кол-во символов): my_string.count('z'): {my_string.count('z')}")  # Outputs: 0

"""
Чтобы проверить, состоит ли строка только из цифр, можно использовать метод isdigit().
Этот метод возвращает True, если все символы в строке являются цифрами, и False
в противном случае. Например:
my_string = '12345'
print(my_string.isdigit())  # Outputs: True
my_string = '123abc'
print(my_string.isdigit())  # Outputs: False

см. пример ниже, где мы проверяем, является ли введенное пользователем значение целым числом, используя метод isdigit(), чтобы не падала ошибка при попытке преобразовать нечисловую строку в целое число. 33-36
"""
my_string = '10'
print(f"isdigit: my_string.isdigit(): {my_string.isdigit()}")  # Outputs: True

integer = input("Enter an integer: ")
if integer.isdigit():
    integer = int(integer)
    print(f"You entered the integer: {integer}")
else:
    print("You did not enter a valid integer.")

