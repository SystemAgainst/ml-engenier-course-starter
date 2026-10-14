# Python Syntax Refresh: 60 минут

Проект — компактный интенсив для быстрого восстановления Python в памяти. Материал
рассчитан на разработчика, которому нужно вспомнить не только «как пишется», но и
ключевые семантические нюансы: мутабельность, truthiness, области видимости,
контракты функций, исключения, модель объектов и безопасную работу с файлами.

## Как пройти за час

| Время | Урок | Что вспомнить |
|---:|---|---|
| 0–7 мин | [01. Переменные и типы](01_lesson_variables_and_types/README.md) | Имена, ссылки, базовые типы, `None`, аннотации, преобразования. |
| 7–17 мин | [02. Коллекции](02_lesson_collections/README.md) | Строки, списки, словари, множества, кортежи, unpacking, comprehensions. |
| 17–25 мин | [03. Условия и циклы](03_lesson_conditions_and_loops/README.md) | `if`, `match`, `for`, `while`, `range`, `enumerate`, `zip`, `break/continue`, loop `else`. |
| 25–35 мин | [04. Функции](04_lesson_functions/README.md) | Виды аргументов, `*args/**kwargs`, области видимости, closures, итераторы. |
| 35–42 мин | [05. Ошибки](05_lesson_error_handling/README.md) | `try/except/else/finally`, точечный перехват, `raise`, chaining, свои исключения. |
| 42–52 мин | [06. Классы и объекты](06_lesson_classes_and_objects/README.md) | Атрибуты, методы, `dataclass`, properties, наследование, протоколы. |
| 52–60 мин | [07. Файлы](07_lesson_files/README.md) | `pathlib`, контекстные менеджеры, text/binary, JSON/CSV, атомарная запись. |

В каждом каталоге есть краткий конспект и `lesson_NN_exercises.py`. Упражнения идут по возрастанию
сложности. Заменяйте `TODO` своим кодом и запускайте файл: проверки на `assert` дают
быструю обратную связь.

## Первичная настройка: Pyenv + Poetry

### Что такое Pyenv и Poetry

- **Pyenv** управляет установленными версиями Python и позволяет выбрать нужную версию для проекта. В этом проекте `.python-version` задаёт Python 3.12, чтобы команды в каталоге проекта использовали именно его.
- **Poetry** управляет зависимостями и виртуальным окружением проекта. Он устанавливает пакеты, указанные в `pyproject.toml`, изолируя их от других проектов; `poetry.lock` фиксирует конкретные версии для повторяемой установки.
- Вместе инструменты разделяют задачи: Pyenv выбирает интерпретатор Python, Poetry создаёт окружение на его основе и управляет пакетами.

### 1. Установить инструменты

macOS с Homebrew:

```bash
brew install pyenv poetry
```

Linux: установите Pyenv и Poetry по их официальным инструкциям, затем перезапустите shell.

### 2. Установить Python и окружение

```bash
cd python_lessons
pyenv install --skip-existing 3.12
pyenv local 3.12
poetry env use "$(pyenv which python)"
poetry install
```

`.python-version` заставляет Pyenv выбирать Python 3.12 в этом каталоге. Poetry создаёт отдельное
виртуальное окружение и ставит Ruff и Mypy из `pyproject.toml`.

### 3. Ежедневная работа

```bash
poetry run python 01_lesson_variables_and_types/lesson_01_exercises.py
poetry run ruff format .
poetry run ruff check . --fix
poetry run mypy .
```

Ruff форматирует код, сортирует импорты и ловит частые ошибки. Mypy не запускает код, а
статически сверяет аннотации типов. Оба инструмента настроены в `pyproject.toml`.
До замены всех `TODO` файлы упражнений намеренно не проходят runtime-проверки. Mypy проверяет
исходный каркас, а после решения — ваши контракты и реализации.

## Как развернуть проект на другой машине

```bash
git clone <repository-url>
cd <repository-directory>/python_lessons
pyenv install --skip-existing "$(cat .python-version)"
pyenv local "$(cat .python-version)"
poetry env use "$(pyenv which python)"
poetry install
poetry run ruff check .
poetry run mypy .
```

После первого `poetry install` Poetry создаст `poetry.lock`. Его следует закоммитить: тогда на
других машинах будут установлены те же версии всех зависимостей.

## Быстрая диагностика

```bash
pyenv version
poetry env info
poetry run python --version
poetry run ruff --version
poetry run mypy --version
```

Если `python` не той версии, проверьте инициализацию Pyenv в shell. Если Poetry привязан к старому
интерпретатору, повторите `poetry env use "$(pyenv which python)"`.
