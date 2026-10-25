from datetime import date
import json
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent / "transactions.json"

class Transaction:
    def __init__(self, *, date: str, category: str, amount: float, description: str) -> None:
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description


    def to_dict(self) -> dict:
        return {
            "date": self.date,
            "category": self.category,
            "amount": self.amount,
            "description": self.description,
        }
        


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


def calculate_by_category(transactions) -> dict:
    totals = {}

    for transaction in transactions:
        category = transaction.category
        amount = transaction.amount

        if category not in totals:
            totals[category] = 0

        totals[category] += amount

    return totals


def filter_by_category(transactions, category):
    filtered_list = []

    for transaction in transactions:
        if transaction.category == category:
            filtered_list.append(transaction)

    return filtered_list


def find_largest_transaction(transactions):
    if not transactions:
        return None

    largest_transaction = transactions[0]

    for transaction in transactions:
        if transaction.amount > largest_transaction.amount:
            largest_transaction = transaction

    return largest_transaction


def save_transactions(transactions, filename):
    with open(filename, "w", encoding="utf-8") as file:
        data = [transaction.to_dict() for transaction in transactions]
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_transactions(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
        transactions = []

        for item in data:
            transaction = Transaction(
                date=item["date"],
                category=item["category"],
                amount=item["amount"],
                description=item["description"],
            )
            transactions.append(transaction)

        return transactions


transactions = load_transactions(DATA_FILE)
empty_transactions = []

# print(expense.to_dict()) # {'date': '2026-10-25', 'category': 'Еда', 'amount': 350, 'description': 'Обед'}

# data = []
# for transaction in transactions:
#     data.append(transaction.to_dict())
# print(data)

while True:
    print("1 — История")
    print("2 — Добавить новый расход")
    print("3 — Общая сумма")
    print("4 — Сводка по категориям")
    print("5 — Фильтр по категории")
    print("6 — Самый крупный расход")
    print("0 — Выход")

    choice = input("Выбор: ")

    if choice == "1":
        show_history(transactions=transactions)
    elif choice == "2":
        add_transaction(transactions=transactions)
    elif choice == "3":
        print(calculate_total(transactions=transactions))
        # print(calculate_total(transactions=empty_transactions))
    elif choice == "4":
        totals = calculate_by_category(transactions)
        if not totals: # totals is None => None означает отсутствие значения => if not totals -> {} — существующий словарь, в котором нет элементов.
            print("Расходов пока нет")
        else:
            for category, amount in totals.items():
                print(f"{category}: {amount:.2f}")
    elif choice == "5":
        category = input("Введите категорию: ").strip()
        filtered_list = filter_by_category(transactions, category=category)
        show_history(filtered_list)
    elif choice == "6":
        largest = find_largest_transaction(transactions=transactions)
        show_history([largest]) # Квадратные скобки здесь создают список из одного объекта, потому что show_history() принимает список.
    elif choice == "0":
        break
    else:
        print("Неизвестная команда")

save_transactions(transactions, DATA_FILE)
