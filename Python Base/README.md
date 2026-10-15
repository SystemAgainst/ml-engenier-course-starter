# Python Base

Основы Python: учебные примеры и домашние задания курса ML Engineering.

Все 23 папки уроков из `python_lessons` размещены непосредственно в этом разделе. Здесь же находятся `pyproject.toml`, `poetry.lock` и `.python-version`.

## Уроки

| Папка | Тема |
|---|---|
| [_01_print](_01_print/) | print |
| [_02_variables](_02_variables/) | variables |
| [_03_int_float](_03_int_float/) | int float |
| [_04_bool](_04_bool/) | bool |
| [_05_if_statement](_05_if_statement/) | if statement |
| [_06_strings](_06_strings/) | strings |
| [_07_lists](_07_lists/) | lists |
| [_08_indexes_slices](_08_indexes_slices/) | indexes slices |
| [_09_for_loop_range](_09_for_loop_range/) | for loop range |
| [_10_functions](_10_functions/) | functions |
| [_11_variables_scope](_11_variables_scope/) | variables scope |
| [_12_while_loop](_12_while_loop/) | while loop |
| [_13_tuples](_13_tuples/) | tuples |
| [_14_dict](_14_dict/) | dict |
| [_15_function_advanced](_15_function_advanced/) | function advanced |
| [_16_json](_16_json/) | json |
| [_17_import](_17_import/) | import |
| [_18_requests](_18_requests/) | requests |
| [_19_comprehensions](_19_comprehensions/) | comprehensions |
| [_20_sets](_20_sets/) | sets |
| [_21_sorted_filter_func](_21_sorted_filter_func/) | sorted filter func |
| [_22_lambda_func](_22_lambda_func/) | lambda func |
| [_23_try_except](_23_try_except/) | try except |
| [_24_classes](_24_classes/) | classes |

## Настройка окружения

Используется Python 3.12. Pyenv выбирает версию Python, а Poetry устанавливает зависимости и создаёт виртуальное окружение.

Из корня репозитория:

```bash
cd "Python Base"
pyenv install --skip-existing "$(cat .python-version)"
poetry env use "$(pyenv which python)"
poetry install
```

## Запуск примеров

```bash
poetry run python _01_print/_1_print_func.py
```

Замените путь на нужный файл урока. Примеры с HTTP-запросами требуют подключения к интернету.

Для форматирования и проверки конкретного решения используйте настроенные Ruff и Mypy:

```bash
poetry run ruff format homework/01_variables/solution.py
poetry run ruff check homework/01_variables/solution.py
poetry run mypy homework/01_variables/solution.py
```

## Домашние задания

Сохраняйте новые работы в [homework](homework/) отдельными папками: `01_topic`, `02_topic` и далее. Каждая работа содержит решение и README по [шаблону](../templates/homework_README.md).

Пример запуска из папки `Python Base` после добавления решения:

```bash
poetry run python homework/01_variables/solution.py
```

Для проверки ментором создайте ветку и Pull Request по [инструкции курса](../README.md).
