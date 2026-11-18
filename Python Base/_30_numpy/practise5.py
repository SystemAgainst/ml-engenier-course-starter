'''Сортировка, поиск и фильтрация'''
import numpy as np


random_matrix = np.random.randint(0, 100, size=(3,3))
print(f"Исходный массив {random_matrix}")

'''
! np.sort возвращает новый массив. Исходный matrix не меняется

'''
sort_by_rows = np.sort(random_matrix, axis=1)
sort_by_cols = np.sort(random_matrix, axis=0)

print(f"\nсортировка по строкам: {sort_by_rows}")
print(f"\nсортировка по колонкам: {sort_by_cols}")

min_row_idx = np.argmin(random_matrix, axis=1)
max_row_idx = np.argmax(random_matrix, axis=1)

print(f"\nиндексы мин/макс элементов в каждой строке: {min_row_idx}/{max_row_idx}")

'''
matrix[mask] всегда возвращает 1D-массив отобранных значений. Форма исходной матрицы теряется. Если нужна матрица с nan на месте отброшенных, используйте np.where.
'''
mask_in_range = random_matrix[(random_matrix > 25) & (random_matrix < 75)]
values_in_range_or_nan = np.where((random_matrix > 25) & (random_matrix < 75), random_matrix, np.nan)

print(f"\nВыбрать все значения между 25 и 75: {mask_in_range}")
print(f"\nматрица с nan на месте отброшенных: {values_in_range_or_nan}")

'''
np.clip(matrix, 25, 75) заменяет всё, что меньше 25, на 25, и всё, что больше 75, на 75. Значения внутри диапазона остаются как есть. Результат — матрица той же формы

clip не меняет исходный массив
'''
clipped = np.clip(random_matrix, 25, 75)
print(f"\nЗаменить значения за пределами диапазона через clip: {clipped}")

'''
np.unique возвращает уникальные значения. С return_counts=True — ещё и число повторов каждого.

np.unique возвращает значения отсортированными по возрастанию. Это поведение по умолчанию.

return_counts=True возвращает кортеж из двух массивов. Их надо распаковать в две переменные

np.unique работает с любой формой, но возвращает 1D-массив. Если нужны уникальные значения по строкам матрицы, используйте axis=0.
'''
data = np.array([3, 1, 2, 3, 1, 3, 2, 4, 4, 1])

values, count = np.unique(data, return_counts=True)
print(f"\nУникальные значения и количество повторений: {values} и {count}")

'''
Скаляр — это одно число
'''
matrix = np.arange(1, 37).reshape(6, 6) 
row_means = matrix.mean(axis=1)
overall_mean = matrix.mean()
mask = row_means > overall_mean # (6,)  True/False ! row_means — форма (6,), overall_mean — скаляр (). Broadcasting выравнивает скаляр с каждым элементом. Получается маска той же формы (6,).
selected = matrix[mask] # (k, 6)  строки, где True

print(f"\nВыбрать строки матрицы, у которых среднее значение выше общего среднего: {selected}")
