'''
Создай классы Transaction и BudgetTracker.
- Transaction должен хранить дату, категорию, сумму и описание
- BudgetTracker должен добавлять и удалять транзакции
- добавь методы расчёта общей суммы и статистики по категориям
- реализуй сохранение и загрузку данных
- добавь понятное строковое представление объектов через __str__
- проверь работу классов на нескольких примерах
'''
import json

class Transaction:
    def __init__(self, *, date: str, category: str, amount: float, description: str) -> None:
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __str__(self) -> str:
        return (
            f"{self.date} | {self.category}: {self.amount:.2f} "
            f"| {self.description}"
        )


class BudgetTracker:
    def __init__(self) -> None:
        self.transactions: list[Transaction] = []

    def add_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)

    def remove_transaction(self, index: int) -> None:
        if index < 0 or index >= len(self.transactions):
            raise IndexError("Транзакции с таким индексом нет")

        self.transactions.pop(index)

    def get_total_amount(self) -> float:
        total = 0.0

        for transaction in self.transactions:
            total += transaction.amount

        return total

    def get_category_statistics(self) -> dict[str, float]:
        result = {}

        for transaction in self.transactions:
            category = transaction.category
            amount = transaction.amount

            if category not in result:
                result[category] = 0.0

            result[category] += amount

        return result

    def save(self, file_path: str) -> None:
        data = []

        for transaction in self.transactions:
            data.append({
                "date": transaction.date,
                "category": transaction.category,
                "amount": transaction.amount,
                "description": transaction.description,
            })

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)


    def load(self, file_path: str) -> None:
        """Загрузить транзакции, заменив текущий список."""
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        loaded_transactions = []

        for item in data:
            transaction = Transaction(
                date=item["date"],
                category=item["category"],
                amount=item["amount"],
                description=item["description"],
            )
            loaded_transactions.append(transaction)

        self.transactions = loaded_transactions



    
transaction = Transaction(date="2026-10-17", category="Еда", amount=350, description="Обед")

print(transaction.date) # 2026-10-17
print(transaction.amount) # 350
print(transaction) # default view because of __str__ – 2026-10-17 | Еда: 350.00 | Обед

print("\n")

tracker = BudgetTracker()
tracker.add_transaction(
    Transaction(
        date="2026-10-17",
        category="Еда",
        amount=350,
        description="Обед",
    )
)
tracker.add_transaction(
    Transaction(
        date="2026-10-17",
        category="Транспорт",
        amount=100,
        description="Метро",
    )
)
tracker.add_transaction(
    Transaction(
        date="2026-10-18",
        category="Развлечения",
        amount=800,
        description="Кино",
    )
)

print(len(tracker.transactions))  # 3
print(tracker.transactions[0])    # Вызовет __str__ транзакции

print(tracker.get_total_amount())  # 1250.0

tracker.remove_transaction(0)  # Удаляем обед за 350
print(tracker.get_total_amount())  # 900.0

print(tracker.get_category_statistics())

print('\n')

tracker.save("transactions.json")

new_tracker = BudgetTracker()
new_tracker.load("transactions.json")

for transaction in new_tracker.transactions:
    print(transaction)

assert new_tracker.get_total_amount() == tracker.get_total_amount()
assert (
    new_tracker.get_category_statistics()
    == tracker.get_category_statistics()
)

print("Сумма и статистика после загрузки совпадают")