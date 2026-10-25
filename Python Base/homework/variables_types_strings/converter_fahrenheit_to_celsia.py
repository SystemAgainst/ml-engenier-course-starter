'''напиши конвертер температуры между градусами Цельсия и Фаренгейта
'''


def convert_data(*, type_of_calculation: int, value: float) -> float:
    if type_of_calculation == 1:
        return (value - 32) * 5 / 9
    elif type_of_calculation == 2:
        return value * 9 / 5 + 32
    else:
        raise ValueError("Нужно выбрать 1 или 2")


try:
    input_type_calculation = int(
        input("1 — из Фаренгейта в Цельсий, 2 — из Цельсия в Фаренгейт: ")
    )
    input_value = float(input("Введите температуру: "))

    result = convert_data(
        type_of_calculation=input_type_calculation,
        value=input_value,
    )
    print(f"Результат: {result:.2f}")
except ValueError as error:
    print(f"Ошибка ввода: {error}")
          