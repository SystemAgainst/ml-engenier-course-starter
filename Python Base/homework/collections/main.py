'''
Возьми список транзакций, где каждая транзакция представлена словарём с полями category, amount и description.
- найди общую сумму расходов ✅
- сгруппируй расходы по категориям ✅
- найди самую крупную и самую маленькую транзакции ✅
- выведи три самые затратные категории ✅
- удали дубликаты описаний с сохранением исходного порядка ✅
- собери множество всех использованных категорий
'''


transactions = [
    {
        "category": "Еда",
        "amount": 350,
        "description": "Обед",
    },
    {
        "category": "Транспорт",
        "amount": 100,
        "description": "Метро",
    },
    {
        "category": "Еда",
        "amount": 200,
        "description": "Кофе",
    },
    {
        "category": "Транспорт",
        "amount": 100,
        "description": "Метро",
    },
    {
        "category": "Развлечения",
        "amount": 800,
        "description": "Кино",
    },
    {
        "category": "Здоровье",
        "amount": 5000,
        "description": "Поход к врачу",
    },
]


def get_max_and_min_transaction(*, transactions: list[dict]) -> dict:
    min_and_max_transaction = {}

    for transaction in transactions:
        amount = transaction['amount']

        if not min_and_max_transaction:
            min_and_max_transaction['min_transaction'] = amount
            min_and_max_transaction['max_transaction'] = amount
        elif amount > min_and_max_transaction['max_transaction']: 
            min_and_max_transaction['max_transaction'] = amount
        elif amount <= min_and_max_transaction['min_transaction']:
            min_and_max_transaction['min_transaction'] = amount

    return min_and_max_transaction


def count_categories(*, transactions: list[dict]) -> dict:
    expenses_by_category = {}

    for transaction in transactions:
        category = transaction['category']
        amount = transaction['amount']

        if category not in expenses_by_category:
            expenses_by_category[category] = 0

        expenses_by_category[category] += amount

    return expenses_by_category


def get_three_most_expenses_category(*, transactions: list[dict]) -> list[str]:
    expenses_by_category = count_categories(transactions=transactions)

    sorted_list = sorted(
        expenses_by_category,
        key=expenses_by_category.get('amount'),
        reverse=True,
    )

    return sorted_list[:3]


def deduplicate_transactions(*, transactions: list[dict]) -> list[dict]:
    deduplicated_list = []
    seen_descriptions = set()

    for transaction in transactions:
        category = transaction['category']

        if category not in seen_descriptions:
            deduplicated_list.append(transaction)
            seen_descriptions.add(category)

    return deduplicated_list


def get_unique_categories(*, transactions: list[dict]) -> set[str]:
    unique_categories = set()

    for transaction in transactions:
        category = transaction['category']
        unique_categories.add(category)

    return unique_categories


sum_of_transactions = 0
for transaction in transactions:
    sum_of_transactions += transaction['amount']

expenses_by_category = count_categories(transactions=transactions)

max_and_min_transaction = get_max_and_min_transaction(transactions=transactions)

three_most_expenses_category = get_three_most_expenses_category(transactions=transactions)

deduplicated_transactions = deduplicate_transactions(transactions=transactions)

unique_categories = get_unique_categories(transactions=transactions)

print(f"Общая сумма расходов: {sum_of_transactions}")
print(f"сгруппируй расходы по категориям: {expenses_by_category}")
print(f"самую крупную и самую маленькую транзакции расходы по категориям: {max_and_min_transaction}")
print(f"выведи три самые затратные категории: {three_most_expenses_category}")
print(f"удали дубликаты описаний с сохранением исходного порядка: {deduplicated_transactions}")
print(f"собери множество всех использованных категорий: {unique_categories}")
