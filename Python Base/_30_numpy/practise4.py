'''Векторизация, ufunc и broadcasting'''
import numpy as np
import time


array = np.array([1, 2, 3, 4, 5])
print(f"вычисли квадрат: {array ** 2}")
print(f"вычисли корень: {np.sqrt(array)}")
print(f"вычисли экспоненту: {np.exp(array)}")
print(f"вычисли логарифм: {np.log(array)}\n")

'''
Нормализовать каждую строку — значит разделить каждый элемент строки на сумму элементов этой строки. После этого сумма каждой строки станет равна 1. В numpy это делается одной векторизованной операцией: сложить по оси 1 (по строкам), затем разделить матрицу на результат. Цикл for не нужен. Ниже — рабочий пример, схема, оговорки про деление на ноль и про оси.

- Нормализация строки — деление каждого элемента строки на сумму элементов этой строки.
- Сумма по оси — matrix.sum(axis=...). Указывает, какую ось «схлопнуть».
- Ось 0 — строки.
- Ось 1 — столбцы.
- keepdims=True — сохранить ось длины 1, чтобы форма результата была совместима с исходной матрицей.
- Broadcasting — автоматическое выравнивание форм при арифметике.
'''
print("нормализация каждой строки матрицы")

matrix = np.arange(1, 37).reshape(6, 6).astype(float)
row_sums = matrix.sum(axis=1, keepdims=True)   # форма (6, 1)
normalized = matrix / row_sums                 # broadcasting: (6,6) / (6,1)

print(normalized)
print(normalized.sum(axis=1))                  # [1. 1. 1. 1. 1. 1.]


'''
Стандартизировать столбец — значит вычесть из каждого элемента среднее этого столбца и разделить на стандартное отклонение этого столбца. После этого каждый столбец имеет среднее 0 и стандартное отклонение 1. В numpy это делается одной векторизованной операцией через broadcasting: (X - mean) / std, где mean и std считаются по оси 0 (по столбцам) с keepdims=True

- Среднее — X.mean(axis=0). Одно число на столбец.
- Стандартное отклонение — X.std(axis=0). Одно число на столбец.
- ddof — «delta degrees of freedom». Поправка знаменателя. ddof=0 — деление на N (по умолчанию в numpy). ddof=1 — деление на N-1 (выборочное).
- Ось 0 — строки. axis=0 схлопывает строки, результат — по столбцам.
- keepdims=True — сохранить ось длины 1, чтобы форма была (1, n).
- Broadcasting — выравнивание форм (m, n) и (1, n).
- Стандартизация (z-score) — (x - mean) / std.
- Дисперсия (variance) — среднее квадратов отклонений.
- Среднее (mean) — сумма чисел, делённая на их количество.
- Отклонение — разность «число минус среднее».
- Квадрат отклонения — отклонение, умноженное само на себя. Всегда неотрицательный.
- Стандартное отклонение (std) — корень из дисперсии.
- axis=0 — считать по каждому столбцу отдельно (идём вниз по строкам).
'''
print(f"\nнормализация каждого столбца матрицы")

X = np.arange(1, 25).reshape(4, 6).astype(float)   # shape (4, 6)

mean = X.mean(axis=0, keepdims=True)   # shape (1, 6)  — средние по столбцам
std  = X.std(axis=0, keepdims=True)    # shape (1, 6)  — std по столбцам

Z = (X - mean) / std                   # broadcasting (4,6)-(1,6) / (1,6)
# Z = (X - X.mean(axis=0, keepdims=True)) / X.std(axis=0, keepdims=True) # короткая запись

print(Z)
print(Z.mean(axis=0))   # ~[0 0 0 0 0 0]
print(Z.std(axis=0))    # ~[1 1 1 1 1 1]

print(f"\nприбавь вектор длины n к каждой строке матрицы m × n")

matrix = np.arange(1, 13).reshape(3, 4) # shape (3,4)
vector = np.array([10, 20, 30, 40]) # shape (4,)

result = matrix + vector
print(result)

print(f"\nвычисли попарные евклидовы расстояния между двумя наборами точек без вложенных циклов")

def pairwise_distances(A, B):
    # A: (m, d), B: (n, d) -> (m, n)
    diff = A[:, None, :] - B[None, :, :]
    return np.sqrt((diff ** 2).sum(axis=2))

A = np.array([[0, 0], [3, 0], [0, 4]], dtype=float)
B = np.array([[0, 0], [3, 4]], dtype=float)

D = pairwise_distances(A, B)
print(D)
print(D.shape)   # (3, 2)

print(f"\nсравни время векторизованного вычисления и Python-цикла на массиве из 1 000 000 элементов")

n = 1_000_000
a = np.arange(n, dtype=np.float64)

# --- векторизованное вычисление ---
t0 = time.perf_counter()
result_np = a * 2 + 1
t_np = time.perf_counter() - t0

# --- цикл Python ---
t0 = time.perf_counter()
result_loop = np.empty(n, dtype=np.float64)
for i in range(n):
    result_loop[i] = a[i] * 2 + 1
t_loop = time.perf_counter() - t0

print(f"numpy:  {t_np:.4f} сек")
print(f"цикл:   {t_loop:.4f} сек")
print(f"ускорение: {t_loop / t_np:.1f}x")
print("результаты совпадают:", np.allclose(result_np, result_loop))