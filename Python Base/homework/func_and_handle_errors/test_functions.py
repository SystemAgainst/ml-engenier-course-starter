import contextlib
import importlib.util
import io
import unittest
from pathlib import Path


def load_module(module_name: str, file_path: Path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module from {file_path}")

    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


homework_dir = Path(__file__).resolve().parent.parent
funcs = load_module("func_and_handle_errors_main", Path(__file__).with_name("main.py"))
conditions = load_module(
    "conditions_cycles_main",
    homework_dir / "conditions_cycles" / "main.py",
)


class FunctionTests(unittest.TestCase):
    def test_safe_divide(self):
        self.assertEqual(funcs.safe_divide(a=10, b=2), 5)
        self.assertEqual(funcs.safe_divide(a=7, b=2), 3.5)
        self.assertEqual(funcs.safe_divide(a=0, b=5), 0)
        self.assertEqual(funcs.safe_divide(a=10, b=-2), -5)

        with self.assertRaises(ZeroDivisionError):
            funcs.safe_divide(a=10, b=0)

        for a, b in [("10", 2), (10, None), (True, 2), (10, False)]:
            with self.subTest(a=a, b=b):
                with self.assertRaises(TypeError):
                    funcs.safe_divide(a=a, b=b)

    def test_validate_transaction(self):
        valid = {
            "category": "Еда",
            "description": "Обед",
            "amount": 350,
        }

        self.assertTrue(funcs.validate_transaction(transaction=valid))
        self.assertTrue(
            funcs.validate_transaction(transaction={**valid, "amount": 0.5})
        )

        invalid_transactions = [
            None,
            {},
            {"category": "Еда", "amount": 100},
            {**valid, "category": ""},
            {**valid, "description": "   "},
            {**valid, "amount": 0},
            {**valid, "amount": -100},
            {**valid, "amount": "350"},
            {**valid, "amount": True},
            {**valid, "amount": float("nan")},
            {**valid, "amount": float("inf")},
        ]

        for transaction in invalid_transactions:
            with self.subTest(transaction=transaction):
                self.assertFalse(
                    funcs.validate_transaction(transaction=transaction)
                )

    def test_get_fizz_buzz(self):
        output = io.StringIO()

        with contextlib.redirect_stdout(output):
            conditions.get_fizz_buzz()

        lines = output.getvalue().splitlines()

        self.assertEqual(len(lines), 100)
        self.assertEqual(lines[0], "1")
        self.assertEqual(lines[2], "Fizz")
        self.assertEqual(lines[4], "Buzz")
        self.assertEqual(lines[14], "FizzBuzz")
        self.assertEqual(lines[-1], "Buzz")

    def test_is_prime(self):
        for number in [2, 3, 7, 17]:
            with self.subTest(number=number):
                self.assertTrue(conditions.is_prime(number))

        for number in [-5, 0, 1, 4, 9, 25]:
            with self.subTest(number=number):
                self.assertFalse(conditions.is_prime(number))

    def test_get_prime_numbers(self):
        self.assertEqual(
            conditions.get_prime_numbers(start=10, end=20),
            [11, 13, 17, 19],
        )
        self.assertEqual(
            conditions.get_prime_numbers(start=2, end=2), [2]
        )
        self.assertEqual(
            conditions.get_prime_numbers(start=-5, end=1), []
        )
        self.assertEqual(
            conditions.get_prime_numbers(start=20, end=10), []
        )

    def test_count_words(self):
        self.assertEqual(
            conditions.count_words("Кот спит, КОТ ест!"),
            {"кот": 2, "спит": 1, "ест": 1},
        )
        self.assertEqual(conditions.count_words(""), {})
        self.assertEqual(conditions.count_words("   \n\t"), {})

    def test_filter_users(self):
        users = [
            {"name": "Аня", "age": 18, "subscription_active": True},
            {"name": "Борис", "age": 17, "subscription_active": True},
            {"name": "Вера", "age": 25, "subscription_active": False},
            {"name": "Глеб", "age": 30, "subscription_active": True},
        ]

        self.assertEqual(
            conditions.filter_users(users=users),
            [users[0], users[3]],
        )
        self.assertEqual(conditions.filter_users(users=[]), [])


if __name__ == "__main__":
    unittest.main()