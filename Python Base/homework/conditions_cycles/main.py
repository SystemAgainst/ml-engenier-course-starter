'''
Условия и циклы
- выведи числа от 1 до 100, заменяя кратные 3 на Fizz, кратные 5 на Buzz, а кратные обоим — на FizzBuzz
- напиши проверку числа на простоту
- найди все простые числа в заданном диапазоне
- реализуй подсчёт частоты слов в тексте без collections.Counter
- отфильтруй список пользователей, оставив только совершеннолетних с активной подпиской
'''

def get_fizz_buzz() -> None:
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


def is_prime(number: int) -> bool:
    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


def get_prime_numbers(*, start: int, end: int) -> list[int]:
    prime_numbers = []

    for number in range(start, end + 1):
        if is_prime(number=number):
            prime_numbers.append(number)

    return prime_numbers


def count_words(text: str) -> dict[str, int]:
    normalized_text = ""

    for character in text.lower():
        if character.isalnum() or character.isspace():
            normalized_text += character
        else:
            normalized_text += " "

    word_counts = {}

    for word in normalized_text.split():
        if word not in word_counts:
            word_counts[word] = 0

        word_counts[word] += 1

    return word_counts


def filter_users(*, users: list[dict]) -> list[dict]:
    filtered_users = []

    for user in users:
        if user['age'] >= 18 and user['subscription_active']:
            filtered_users.append(user)

    return filtered_users


print(get_fizz_buzz())
print("\n")

print(is_prime(10))
print("\n")

print(get_prime_numbers(start=10, end=20))
print("\n")

print(count_words("Кот спит, кот ест!")) # # {"кот": 2, "спит": 1, "ест": 1}
print("\n")

users = [
    {"name": "Аня", "age": 20, "subscription_active": True},
    {"name": "Борис", "age": 17, "subscription_active": True},
    {"name": "Вера", "age": 25, "subscription_active": False},
]
print(filter_users(users=users))