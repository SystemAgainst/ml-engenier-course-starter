'''
Домашнее задание: трекер расходов
Собери небольшую консольную программу на чистом Python без Pandas и других библиотек для анализа данных. Пользователь должен уметь добавлять расходы, смотреть историю и получать сводку по категориям.

// Обязательные требования
//////////////////////////
- меню с несколькими действиями работает в цикле до команды выхода
- каждая транзакция содержит дату, категорию, сумму и комментарий
- ввод валидируется, ошибки не завершают программу аварийно
- данные сохраняются между запусками в JSON или CSV
- можно вывести общую сумму и разбивку по категориям
- можно найти самую крупную транзакцию и отфильтровать расходы по категории
- логика разделена на функции и классы, нет одного огромного блока кода
- в репозитории есть README.md с инструкцией запуска и примерами использования

// Дополнительное усложнение
////////////////////////////

- добавь месячный лимит и предупреждение о его превышении
- реализуй редактирование и удаление транзакций
- добавь сортировку по дате и сумме
- покрой ключевые функции несколькими тестами через pytest
'''

1 этап написали и вывели экземпляр класса:
```
class Transaction:
    def __init__(self, *, date: str, category: str, amount: float, description: str) -> None:
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description
    

expense = Transaction(date="2026-10-25", category="Еда", amount=350, description="Обед")
print(expense.date)
```

2 этап – создания списка транзакций и вывод двух транзакций:
```
class Transaction:
    def __init__(self, *, date: str, category: str, amount: float, description: str) -> None:
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description


def show_history(transactions):
    if not transactions:
        print("Расходов пока нет")
    else:  
        for transaction in transactions:
            print(f"{transaction.date} | {transaction.category} | {transaction.amount} | {transaction.description}")
    

expense = Transaction(date="2026-10-25", category="Еда", amount=350, description="Обед")

expense2 = Transaction(date="2026-10-25", category="Транспорт", amount=120, description="Поездка на автобусе")

transactions = []
empty_transactions = []
transactions.append(expense)
transactions.append(expense2)

show_history(transactions)
show_history(transactions=empty_transactions)
```

3 этап - пользователь сам показать историю и/или выйти в бесконечном цикле
```
class Transaction:
    def __init__(self, *, date: str, category: str, amount: float, description: str) -> None:
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description


def show_history(transactions):
    if not transactions:
        print("Расходов пока нет")
    else:  
        for transaction in transactions:
            print(f"{transaction.date} | {transaction.category} | {transaction.amount} | {transaction.description}")
    

expense = Transaction(date="2026-10-25", category="Еда", amount=350, description="Обед")

expense2 = Transaction(date="2026-10-25", category="Транспорт", amount=120, description="Поездка на автобусе")

transactions = []
empty_transactions = []
transactions.append(expense)
transactions.append(expense2)

while True:
    print("1 — История")
    print("0 — Выход")

    choice = input("Выбор: ")

    if choice == "1":
        show_history(transactions=transactions)
    elif choice == "0":
        break
    else:
        print("Неизвестная команда")
```

4 Этап – добавим ввод нового расхода через функцию add_transaction(transactions)
```class Transaction:
    def __init__(self, *, date: str, category: str, amount: float, description: str) -> None:
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description


def show_history(transactions):
    if not transactions:
        print("Расходов пока нет")
    else:  
        for transaction in transactions:
            print(f"{transaction.date} | {transaction.category} | {transaction.amount} | {transaction.description}")


def add_transaction(transactions):
    new_date = input("Введите дату: ")
    new_category = input("Введите категорию: ")
    new_amount = float(input("Введите сумму: "))
    new_description = input("Введите описание: ")

    new_transaction = Transaction(date=new_date, category=new_category, amount=new_amount, description=new_description)

    transactions.append(new_transaction)
    print("Новая транзакция добавлена")

    
expense = Transaction(date="2026-10-25", category="Еда", amount=350, description="Обед")

expense2 = Transaction(date="2026-10-25", category="Транспорт", amount=120, description="Поездка на автобусе")

transactions = []
empty_transactions = []
transactions.append(expense)
transactions.append(expense2)

while True:
    print("1 — История")
    print("2 — Добавить новый расход")
    print("0 — Выход")

    choice = input("Выбор: ")

    if choice == "1":
        show_history(transactions=transactions)
    elif choice == "2":
        add_transaction(transactions=transactions)
    elif choice == "0":
        break
    else:
        print("Неизвестная команда")
```

5 Этап, добавить обработку ошибки, чтобы при вводе в amount 'abc', программа не ломалась
```
from datetime import date


class Transaction:
    def __init__(self, *, date: str, category: str, amount: float, description: str) -> None:
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description


def show_history(transactions):
    if not transactions:
        print("Расходов пока нет")
    else:  
        for transaction in transactions:
            print(f"{transaction.date} | {transaction.category} | {transaction.amount} | {transaction.description}")


def add_transaction(transactions):
    while True:
        try:
            new_date = input("Введите дату: ").strip()
            date.fromisoformat(new_date)
            break
        except ValueError:
            print("формат ГГГГ-ММ-ДД. например, 2026-02-30 недопустима. ")

    while True:
        new_category = input("Введите категорию: ").strip()

        if new_category:
            break
        else:
            print("Категория не должна быть пустой")

    while True:
        try:
            new_amount = float(input("Введите сумму: "))
            if new_amount > 0:
                break
            else:
                print("Сумма должна быть больше нуля")
        except ValueError:
            print("Введите число, например 150.50")
    
    new_description = input("Введите описание: ")
            

    new_transaction = Transaction(date=new_date, category=new_category, amount=new_amount, description=new_description)

    transactions.append(new_transaction)
    print("Новая транзакция добавлена")

    
expense = Transaction(date="2026-10-25", category="Еда", amount=350, description="Обед")

expense2 = Transaction(date="2026-10-25", category="Транспорт", amount=120, description="Поездка на автобусе")

transactions = []
empty_transactions = []
transactions.append(expense)
transactions.append(expense2)

while True:
    print("1 — История")
    print("2 — Добавить новый расход")
    print("0 — Выход")

    choice = input("Выбор: ")

    if choice == "1":
        show_history(transactions=transactions)
    elif choice == "2":
        add_transaction(transactions=transactions)
    elif choice == "0":
        break
    else:
        print("Неизвестная команда")
```

6 этап – добавить функ для подсчета итоговых затрат
```
from datetime import date


class Transaction:
    def __init__(self, *, date: str, category: str, amount: float, description: str) -> None:
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description


def show_history(transactions):
    if not transactions:
        print("Расходов пока нет")
    else:  
        for transaction in transactions:
            print(f"{transaction.date} | {transaction.category} | {transaction.amount} | {transaction.description}")


def add_transaction(transactions):
    while True:
        try:
            new_date = input("Введите дату: ").strip()
            date.fromisoformat(new_date)
            break
        except ValueError:
            print("формат ГГГГ-ММ-ДД. например, 2026-02-30 недопустима. ")

    while True:
        new_category = input("Введите категорию: ").strip()

        if new_category:
            break
        else:
            print("Категория не должна быть пустой")

    while True:
        try:
            new_amount = float(input("Введите сумму: "))
            if new_amount > 0:
                break
            else:
                print("Сумма должна быть больше нуля")
        except ValueError:
            print("Введите число, например 150.50")
    
    new_description = input("Введите описание: ")
            

    new_transaction = Transaction(date=new_date, category=new_category, amount=new_amount, description=new_description)

    transactions.append(new_transaction)
    print("Новая транзакция добавлена")


def calculate_total(transactions) -> float:
    total = 0

    for transaction in transactions:
        total += transaction.amount

    return total

    
expense = Transaction(date="2026-10-25", category="Еда", amount=350, description="Обед")

expense2 = Transaction(date="2026-10-25", category="Транспорт", amount=120, description="Поездка на автобусе")

transactions = []
empty_transactions = []
transactions.append(expense)
transactions.append(expense2)

while True:
    print("1 — История")
    print("2 — Добавить новый расход")
    print("3 — Общая сумма")
    print("0 — Выход")

    choice = input("Выбор: ")

    if choice == "1":
        show_history(transactions=transactions)
    elif choice == "2":
        add_transaction(transactions=transactions)
    elif choice == "3":
        print(calculate_total(transactions=transactions))
        print(calculate_total(transactions=empty_transactions))
    elif choice == "0":
        break
    else:
        print("Неизвестная команда")
```

7 этап – сводка по категориям:
```
...
def calculate_by_category(transactions) -> dict:
    totals = {}

    for transaction in transactions:
        category = transaction.category
        amount = transaction.amount

        if category not in totals:
            totals[category] = 0
            
        totals[category] += amount

    return totals
...
```

8 Этап – find_largest_transaction
```
def find_largest_transaction(transactions):
    if not transactions:
        return None

    largest_transaction = transactions[0]

    for transaction in transactions:
        if transaction.amount > largest_transaction.amount:
            largest_transaction = transaction

    return largest_transaction
```