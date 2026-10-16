x = 42
y = x
print(id(x)) # 4321339200 – id возвращает ячейку памяти, в к-ой хранится x

print(id(y)) # ячейка памяти x и y совпадают => x и y ссылаются на одну ячейку памяти

print("\n")

'''числа при изменении кладутся в другую ячейку памяти'''
print(id(x), id(y), x, y)
y += 1
print(id(x), id(y), x, y)

print("\n")

'''
Неизменяемые структуры данных, однажды будучи инициированной не может быть изменена. Если изменяем, то создается новый объект, в новой ячейке памяти и переменная ссылается уже на новый объект и новую ячейку памяти.
'''
my_list = [1,2,3]
another_list = my_list
print(id(my_list), id(another_list))

print("\n")

print(id(my_list), id(another_list), my_list, another_list)
another_list.append(4)
print(id(my_list), id(another_list), my_list, another_list)

print("\n")

'''
Неизменяемые типы данных: int, str, float, tuple, bool, None...
Изменяемые типы данных: list, dict, set
'''

'''проверка на то, что объекты ссылаются на одну и ту же ячейку памяти – есть ключевое слово is'''
a = None
b = None
print(a is b) # True

print("\n")

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
print(list1 is list2) # True
print(list1 == list3) # True, т.к. их длина и очередность равна
print(id(list1), id(list3)) # list 1 - 4373139584, list3 - 4373440448
print(list1 is list3) # False, т.к. они ссылаются на отдельные ячейки памяти (см.на строку выше)

print("\n")

'''Сравнение с None и булевыми значениями:

- Singleton (одиночка) — объект или экземпляр класса, который по задумке существует в единственном экземпляре и используется из разных частей программы. 

В Python None — singleton: сколько бы переменных ни получили значение None, они ссылаются на один и тот же объект. Поэтому None проверяют через is / is not: это проверка идентичности.
- Наглядный контраст: два отдельных вызова object() создают два разных объекта, даже если сами объекты ничем не отличаются.
- Для обычного условия с bool обычно используют само значение: if some_variable.

Это идиоматично и проверяет truthiness (истинность) значения.
- `is True` нужен редко — только если важно, что значение именно объект True,
  а не просто truthy-объект.
- `== True` сравнивает на равенство и может дать True не только для bool: например, в Python `1 == True` равно True. Поэтому сравнение с True обычно не нужно; PEP 8 рекомендует писать `if some_variable`, а не `if some_variable == True`.
'''
some_variable = True
some_variable_none = None
another_none = None
print(some_variable == True)  # True, но обычно так не пишут (PEP 8, E712)
print(some_variable_none is None)  # True: проверка идентичности с None
print(some_variable_none is another_none)  # True: оба имени ссылаются на singleton None
print(some_variable is True)  # True: проверка на точный объект True

first_object = object()
second_object = object()
print(first_object is second_object)  # False: созданы два разных объекта

if some_variable:
    print("Условие истинно")  # Рекомендуемый стиль для обычной проверки bool

print(1 == True)  # True: == сравнивает значения, а не тип/идентичность 
one = 1
print(one is True)  # False: 1 и True — разные объекты