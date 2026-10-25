"""Save transactions as JSON and export their statistics as CSV."""

import csv
import json
from pathlib import Path
from typing import TypedDict

Transaction = dict[str, object]


class CategoryStatistics(TypedDict):
    transaction_count: int
    total_amount: int | float


class StatisticsRow(TypedDict):
    category: str
    transaction_count: int
    total_amount: int | float


def save_transactions(*, transactions: list[Transaction], file_path: str | Path) -> None:
    """Write transactions to a UTF-8 JSON file."""
    with Path(file_path).open("w", encoding="utf-8") as file:
        json.dump(transactions, file, ensure_ascii=False, indent=2)


def load_transactions(*, file_path: str | Path) -> list[Transaction]:
    """Read transactions from JSON, raising clear errors for missing or invalid files."""
    path = Path(file_path)
    try:
        with path.open(encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError as error:
        raise FileNotFoundError(f"Файл с транзакциями не найден: {path}") from error
    except json.JSONDecodeError as error:
        raise ValueError(f"Файл содержит некорректный JSON: {path}") from error

    if not isinstance(data, list) or any(not isinstance(item, dict) for item in data):
        raise ValueError(f"JSON-файл должен содержать список транзакций: {path}")

    return data


def verify_transactions_round_trip(
    *,
    transactions: list[Transaction],
    file_path: str | Path,
) -> bool:
    """Save and reload transactions, then compare the data with the original."""
    save_transactions(transactions=transactions, file_path=file_path)
    return load_transactions(file_path=file_path) == transactions


def get_transaction_statistics(*, transactions: list[Transaction]) -> list[StatisticsRow]:
    """Return transaction counts and spending totals by category and overall."""
    category_statistics: dict[str, CategoryStatistics] = {}

    for transaction in transactions:
        category = transaction.get("category")
        amount = transaction.get("amount")
        if not isinstance(category, str) or not category.strip():
            raise ValueError("У каждой транзакции должна быть заполнена категория")
        if isinstance(amount, bool) or not isinstance(amount, int | float):
            raise ValueError("Сумма каждой транзакции должна быть числом")

        if category not in category_statistics:
            category_statistics[category] = {"transaction_count": 0, "total_amount": 0}

        category_statistics[category]["transaction_count"] += 1
        category_statistics[category]["total_amount"] += amount

    statistics: list[StatisticsRow] = [
        {
            "category": category,
            "transaction_count": values["transaction_count"],
            "total_amount": values["total_amount"],
        }
        for category, values in sorted(category_statistics.items())
    ]
    total_amount = sum(values["total_amount"] for values in category_statistics.values())
    statistics.append(
        {
            "category": "Итого",
            "transaction_count": len(transactions),
            "total_amount": total_amount,
        }
    )
    return statistics


def export_statistics_to_csv(
    *,
    transactions: list[Transaction],
    file_path: str | Path,
) -> None:
    """Export transaction counts and spending totals to a UTF-8 CSV file."""
    statistics = get_transaction_statistics(transactions=transactions)
    fieldnames = ["category", "transaction_count", "total_amount"]

    with Path(file_path).open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(statistics)

if __name__ == "__main__":
    import tempfile

    transactions = [
        {"category": "Еда", "amount": 350, "description": "Обед"},
        {"category": "Еда", "amount": 200, "description": "Кофе"},
        {"category": "Транспорт", "amount": 100, "description": "Метро"},
    ]

    with tempfile.TemporaryDirectory() as folder:
        folder_path = Path(folder)

        json_path = folder_path / "transactions.json"
        csv_path = folder_path / "statistics.csv"

        # 1. Сохранение и чтение JSON
        save_transactions(
            transactions=transactions,
            file_path=json_path,
        )
        loaded = load_transactions(file_path=json_path)

        assert loaded == transactions, "Данные изменились"
        print("OK: сохранение и чтение JSON")

        # 2. Функция проверки сохранения
        assert verify_transactions_round_trip(
            transactions=transactions,
            file_path=json_path,
        )
        print("OK: проверка совпадения данных")

        # 3. Расчёт статистики
        expected_statistics = [
            {"category": "Еда", "transaction_count": 2, "total_amount": 550},
            {"category": "Транспорт", "transaction_count": 1, "total_amount": 100},
            {"category": "Итого", "transaction_count": 3, "total_amount": 650},
        ]

        assert (
            get_transaction_statistics(transactions=transactions)
            == expected_statistics
        )
        print("OK: расчёт статистики")

        # 4. Экспорт и чтение CSV
        export_statistics_to_csv(
            transactions=transactions,
            file_path=csv_path,
        )

        with csv_path.open(encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            assert reader.fieldnames == [
                "category", "transaction_count", "total_amount"
            ]
            rows = list(reader)

        # В CSV числа читаются как строки.
        assert rows == [
            {"category": "Еда", "transaction_count": "2", "total_amount": "550"},
            {"category": "Транспорт", "transaction_count": "1", "total_amount": "100"},
            {"category": "Итого", "transaction_count": "3", "total_amount": "650"},
        ]
        print("OK: экспорт CSV")

        # 5. Отсутствующий файл
        try:
            load_transactions(file_path=folder_path / "missing.json")
        except FileNotFoundError:
            print("OK: отсутствующий файл обработан")
        else:
            raise AssertionError("Ожидалась ошибка FileNotFoundError")

        # 6. Некорректный JSON
        broken_path = folder_path / "broken.json"
        broken_path.write_text("это не JSON", encoding="utf-8")

        try:
            load_transactions(file_path=broken_path)
        except ValueError:
            print("OK: некорректный JSON обработан")
        else:
            raise AssertionError("Ожидалась ошибка ValueError")

        # 7. JSON с неправильной структурой
        wrong_path = folder_path / "wrong_structure.json"
        wrong_path.write_text('{"category": "Еда"}', encoding="utf-8")

        try:
            load_transactions(file_path=wrong_path)
        except ValueError:
            print("OK: неправильная структура JSON обработана")
        else:
            raise AssertionError("Ожидалась ошибка ValueError")

        # 8. Пустой список
        assert verify_transactions_round_trip(
            transactions=[],
            file_path=json_path,
        )
        assert get_transaction_statistics(transactions=[]) == [
            {"category": "Итого", "transaction_count": 0, "total_amount": 0},
        ]
        print("OK: пустой список")

    print("\nВсе проверки пройдены!")