'''запроси у пользователя имя, возраст и город, затем сформируй аккуратное сообщение через f-string
'''


def get_message(*, name: str, age: int, city: str) -> str:
    return f"Your data: name - {name}, age - {age}, city - {city}"


name = input(f"Enter your name: ")
age = int(input(f"Enter your age: "))
city = input(f"Enter your city: ")

shaped_message = get_message(name=name, age=age, city=city)
print(shaped_message)
