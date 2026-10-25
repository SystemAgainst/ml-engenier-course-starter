'''
- вынеси решения предыдущих задач в небольшие функции 
- добавь type hints и короткие docstrings
- напиши функцию safe_divide(a, b), которая корректно обрабатывает неверные типы и деление на ноль
- создай функцию валидации транзакции: сумма должна быть положительной, а обязательные поля — заполнены
- протестируй функции на обычных, граничных и ошибочных входных данных
'''
import math

def safe_divide(*, a: int | float, b: int | float) -> float:
    if isinstance(a, bool) or not isinstance(a, int | float):
        raise TypeError("a должно быть числом int или float")

    if isinstance(b, bool) or not isinstance(b, int | float):
        raise TypeError("b должно быть числом int или float")

    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")

    return a / b


def validate_transaction(*, transaction: object) -> bool:
    if not isinstance(transaction, dict):
        return False

    for field in ("category", "description"):
        value = transaction.get(field)

        if not isinstance(value, str) or not value.strip():
            return False

        amount = transaction.get("amount")

        if isinstance(amount, bool) or not isinstance(amount, int | float):
            return False

        if isinstance(amount, float) and not math.isfinite(amount):
            return False

    return amount > 0
    


test_data = {
    "category": "Еда",
    "description": "Обед",
    "amount": 350,
}

print(validate_transaction(transaction=test_data))