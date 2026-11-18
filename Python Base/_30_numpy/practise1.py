import numpy as np

array = np.array([1, 2, 3, 4, 5])
arange = np.arange(1, 6, 1)
linspace = np.linspace(1, 5, 5)

print(f"array: {array}, arange: {arange}, linspace: {linspace}")

zeros_matrix = np.zeros((3, 3), dtype=int)
ones_matrix = np.ones((3, 3), dtype=int)
random_matrix = np.random.randint(0, 10, size=(3, 3))

print(f"Матрица из нулей:\n{zeros_matrix}")
print(f"Матрица из единиц:\n{ones_matrix}")
print(f"Матрица из случайных чисел:\n{random_matrix}")

pairs = (
    ("array", array),
    ("random_matrix", random_matrix),
)
for name, values in pairs:
    print(f"\nХарактеристики {name}:")
    print(f"shape: {values.shape}")
    print(f"ndim: {values.ndim}")
    print(f"size: {values.size}")
    print(f"dtype: {values.dtype}")
    print(f"Занимаемая память: {values.nbytes} байт")

array_from_int_to_float = np.array(array, dtype=np.float32)
print(f"\nИсходный целочисленный массив: {array} ({array.nbytes} байт) vs преобразованный массив: {array_from_int_to_float} ({array_from_int_to_float.nbytes} байт))")

'''
Единичная матрица — квадратная матрица, у которой на главной диагонали стоят 1, а остальные элементы равны 0.

Диагональная матрица — квадратная матрица, у которой все элементы вне главной диагонали равны 0. На диагонали могут стоять любые числа.

Единичная матрица — это частный случай диагональной матрицы
'''
identity_matrix_eye = np.eye(3)
identity_matrix_identity = np.identity(3)
identity_matrix_from_diagonal = np.diag([1, 1, 1])

print(f"\nЕдиничная матрица через np.eye:\n{identity_matrix_eye}")
print(f"\nЕдиничная матрица через np.identity:\n{identity_matrix_identity}")
print(f"\nМатрица через np.diag:\n{identity_matrix_from_diagonal}")