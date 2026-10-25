import csv
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from homework.files_and_serialization.main import (
    export_statistics_to_csv,
    get_transaction_statistics,
    load_transactions,
    save_transactions,
    verify_transactions_round_trip,
)


class TransactionSerializationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.json_path = Path(self.temp_dir.name) / "transactions.json"

    def test_save_and_load_preserves_transaction_data(self) -> None:
        transactions = [
            {"category": "Еда", "amount": 350, "description": "Обед"},
            {"category": "Транспорт", "amount": 100.5, "description": "Метро"},
        ]

        save_transactions(transactions=transactions, file_path=self.json_path)

        self.assertEqual(load_transactions(file_path=self.json_path), transactions)

    def test_round_trip_verification_succeeds(self) -> None:
        transactions = [{"category": "Еда", "amount": 350, "description": "Обед"}]

        self.assertTrue(
            verify_transactions_round_trip(
                transactions=transactions,
                file_path=self.json_path,
            )
        )

    def test_missing_json_file_raises_clear_error(self) -> None:
        with self.assertRaisesRegex(FileNotFoundError, "не найден"):
            load_transactions(file_path=self.json_path)

    def test_malformed_json_raises_clear_error(self) -> None:
        self.json_path.write_text("{broken", encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "некорректный JSON"):
            load_transactions(file_path=self.json_path)

    def test_json_with_invalid_transaction_structure_is_rejected(self) -> None:
        self.json_path.write_text('{"category": "Еда"}', encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "список транзакций"):
            load_transactions(file_path=self.json_path)


class TransactionStatisticsTests(unittest.TestCase):
    def test_statistics_include_category_and_overall_totals(self) -> None:
        transactions = [
            {"category": "Еда", "amount": 350, "description": "Обед"},
            {"category": "Транспорт", "amount": 100, "description": "Метро"},
            {"category": "Еда", "amount": 200, "description": "Кофе"},
        ]

        self.assertEqual(
            get_transaction_statistics(transactions=transactions),
            [
                {"category": "Еда", "transaction_count": 2, "total_amount": 550},
                {"category": "Транспорт", "transaction_count": 1, "total_amount": 100},
                {"category": "Итого", "transaction_count": 3, "total_amount": 650},
            ],
        )

    def test_empty_statistics_have_zero_overall_totals(self) -> None:
        self.assertEqual(
            get_transaction_statistics(transactions=[]),
            [{"category": "Итого", "transaction_count": 0, "total_amount": 0}],
        )

    def test_statistics_reject_invalid_category_or_amount(self) -> None:
        invalid_transactions: list[dict[str, object]] = [
            {"category": "", "amount": 1},
            {"category": "Еда", "amount": "1"},
            {"category": "Еда", "amount": True},
        ]

        for transaction in invalid_transactions:
            with (
                self.subTest(transaction=transaction),
                self.assertRaises(ValueError),
            ):
                get_transaction_statistics(transactions=[transaction])

    def test_csv_export_contains_category_and_overall_statistics(self) -> None:
        transactions = [
            {"category": "Еда", "amount": 350, "description": "Обед"},
            {"category": "Еда", "amount": 200, "description": "Кофе"},
        ]
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_path = Path(temp_dir) / "statistics.csv"

            export_statistics_to_csv(
                transactions=transactions,
                file_path=csv_path,
            )

            with csv_path.open(encoding="utf-8", newline="") as file:
                rows = list(csv.DictReader(file))

        self.assertEqual(
            rows,
            [
                {"category": "Еда", "transaction_count": "2", "total_amount": "550"},
                {"category": "Итого", "transaction_count": "2", "total_amount": "550"},
            ],
        )


if __name__ == "__main__":
    unittest.main()
