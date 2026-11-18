'''Сортировка, поиск и фильтрация'''
import numpy as np

'''
42. Внутри — алгоритм PCG64 (современный алгоритм генерации псевдослучайных чисел).

42 — произвольное число. Оно не имеет специального смысла в numpy. Это традиция.
'''
rng = np.random.default_rng(seed=42) 
matrix = rng.normal(size=(5, 4))
print(f"Воспроизводимая выборка: {matrix}")

print(f"\nСумма: {matrix.sum()}")
print(f"Среднее: {matrix.mean()}")
print(f"Медиана: {np.median(matrix)}")
print(f"Дисперсия: {matrix.var()}")
print(f"Стандартное отклонение: {matrix.std()}")
print(f"25-й перцентиль: {np.percentile(matrix, 25)}")
print(f"Квартили (25/50/75): {np.percentile(matrix, [25, 50, 75])}")

print(f"\nвычисления отдельно по строкам и столбцам: ")

print("\n--- По столбцам (axis=0) ---")
print(f"\nСумма: {matrix.sum(axis=0)}")
print(f"Среднее: {matrix.mean(axis=0)}")
print(f"Медиана: {np.median(matrix, axis=0)}")
print(f"Дисперсия: {matrix.var(axis=0)}")
print(f"Стандартное отклонение: {matrix.std(axis=0)}")
print(f"25-й перцентиль: {np.percentile(matrix, 25, axis=0)}")
print(f"Квартили (25/50/75): {np.percentile(matrix, [25, 50, 75], axis=0)}")

print("\n--- По строкам (axis=1) ---")
print(f"\nСумма: {matrix.sum(axis=1)}")
print(f"Среднее: {matrix.mean(axis=1)}")
print(f"Медиана: {np.median(matrix, axis=1)}")
print(f"Дисперсия: {matrix.var(axis=1)}")
print(f"Стандартное отклонение: {matrix.std(axis=1)}")
print(f"25-й перцентиль: {np.percentile(matrix, 25, axis=1)}")
print(f"Квартили (25/50/75): {np.percentile(matrix, [25, 50, 75], axis=1)}")

'''
NaN «заражает» обычную арифметику: любая операция с NaN даёт NaN. Поэтому mean, median, std при наличии NaN возвращают NaN. Функции nan* игнорируют NaN и считают по остальным.


! nanmean делит на число не-NaN элементов. nanmean([1, 2, NaN]) = (1+2)/2 = 1.5, а не (1+2+0)/3.

!! если все значения NaN, nanmean вернёт nan и предупреждение RuntimeWarning: Mean of empty slice

!!! NaN нельзя проверять через ==. np.nan == np.nan даёт False. Только np.isnan
'''
data = rng.normal(size=100)
data[::10] = np.nan        # каждое 10-е значение = NaN => итого 10 NaN из 100

print("--- обычные функции (с NaN) ---")
print(f"mean: {data.mean()}") # NaN
print(f"median: {np.median(data)}") # NaN
print(f"std: {data.std()}") # NaN

print("\n--- nan-функции (игнорируют NaN) ---")
print(f"nanmean: {np.nanmean(data)}") # число
print(f"nanmedian: {np.nanmedian(data)}") # число
print(f"nanstd: {np.nanstd(data)}") # число

print(f"\n число NaN: {np.isnan(data).sum()}") # 10

sample = rng.normal(loc=0, scale=1, size=10000)
mean, std = sample.mean(), sample.std()
print(f"\nmean={mean:.3f}, std={std:.3f}")
'''
Шаг 1. sample - mean
Вычитаем среднее из каждого элемента. Это центрирование: сдвигаем данные так, чтобы среднее стало 0

Шаг 2. np.abs(...)
Модуль убирает знак. Теперь каждое число — это расстояние от среднего, без направления.

Шаг 3. ... <= k * std
Сравниваем каждое расстояние с порогом k * std. Результат — маска True/False той же формы.

Шаг 4. np.mean(mask)
Среднее из True/False. В numpy True = 1, False = 0. Среднее из нулей и единиц — это доля единиц.

Шаг 5. frac = ...
Результат сохраняется в переменную frac (сокращение от «fraction» — доля); σ — греческая буква «сигма»
'''
for k in (1, 2, 3):
    frac = np.mean(np.abs(sample - mean) <= k * std)
    print(f"±{k}σ: {frac:.4f}")
