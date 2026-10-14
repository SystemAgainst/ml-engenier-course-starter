# ml-engenier-course-starter

Учебный репозиторий курса по ML Engineering: материалы, практика и домашние задания для проверки ментором.

## Структура

```text
ml-engenier-course-starter/
├── Python Base/          # Основы Python и домашние задания
│   └── homework/
├── Mathematics/          # Математика для машинного обучения
│   └── homework/
├── SQL/                  # Базы данных и SQL
│   └── homework/
├── Data Analysis/        # NumPy, pandas и работа с данными
│   └── homework/
├── Machine Learning/     # Модели, обучение и оценка качества
│   └── homework/
├── python_lessons/       # Уже имеющиеся уроки и примеры Python
└── templates/            # Шаблон описания домашнего задания
```

## Разделы курса

| Раздел | Содержание |
|---|---|
| [Python Base](Python%20Base/README.md) | Типы данных, коллекции, условия, циклы, функции, модули и исключения |
| [Mathematics](Mathematics/README.md) | Линейная алгебра, математический анализ, теория вероятностей и статистика |
| [SQL](SQL/README.md) | Выборки, JOIN, агрегирование, подзапросы и оконные функции |
| [Data Analysis](Data%20Analysis/README.md) | Подготовка данных, исследовательский анализ и визуализация |
| [Machine Learning](Machine%20Learning/README.md) | Обучение моделей, метрики, валидация и практические проекты |

Разделы — основа для организации учебных работ; задания добавляются по мере прохождения курса. Новые темы можно добавлять отдельными папками.

## Как оформить домашнее задание

Для каждой работы создайте отдельную папку в `homework` соответствующего раздела, например:

```text
Python Base/homework/01_variables/
├── README.md       # Условие, описание решения и инструкция запуска
└── solution.py     # Решение
```

Скопируйте [шаблон](templates/homework_README.md) в README задания. Добавьте исходное условие, решение, необходимые зависимости, способ запуска и вопросы ментору. Для математики можно приложить PDF или notebook, для SQL — файл `solution.sql` и описание схемы и исходных данных.

## Как сдавать работу ментору

1. Создайте ветку для задания, например `homework/python-01`.
2. Добавьте решение и README в папку соответствующего раздела.
3. Проверьте запуск по инструкции из README задания.
4. Сделайте commit, отправьте ветку на GitHub и откройте Pull Request в `main`.
5. Передайте ментору ссылку на Pull Request. Исправления добавляйте в ту же ветку, чтобы сохранить обсуждение.
6. После проверки объедините Pull Request с `main`.

Пример команд из корня репозитория:

```bash
git switch -c homework/python-01
git add "Python Base/homework/01_variables"
git commit -m "Add Python homework 01"
git push -u origin homework/python-01
```

## Запуск существующих уроков Python

В `python_lessons` сохранены настройки Python 3.12 и зависимости Poetry.

```bash
cd python_lessons
poetry install
poetry run python _01_print/_1_print_func.py
```

Для нового задания указывайте команды запуска и зависимости в его README. Выполняйте Python-задания из окружения с нужными пакетами, например:

```bash
cd python_lessons
poetry run python "../Python Base/homework/01_variables/solution.py"
```

В Git сохраняются исходники, notebook, небольшие учебные данные и описания работ. Виртуальные окружения, кэш, локальные секреты и крупные наборы данных исключены через `.gitignore`. Для внешних данных указывайте источник и инструкцию получения в README задания.
