'''реализуй простой калькулятор для операций +-/*'''


def get_math_operation(*, a: float, operator: str, b: float) -> float:
    if operator == "+":
        return a+b
    if operator == "-":
        return a-b
    if operator == "*":
        return a*b
    if operator == "/":
        if b == 0:
            raise ValueError("Деление на ноль")
        else:
            return a / b 
    else:
        raise ValueError(f"Неизвестный оператор: {operator}")


try:
    a = float(input("Enter a: "))
    operator = input("Enter operator (+, -, *, /): ").strip()
    b = float(input("Enter b: "))

    result = get_math_operation(a=a, operator=operator, b=b)
    print(f"Результат: {result}")

except ValueError as error:
    print(f"Ошибка ввода: {error}")


