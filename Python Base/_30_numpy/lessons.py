import numpy as np

'''
1-ый способ создания массива
'''
data = [1, 2, 3, 4, 5]

arr = np.array(data) # создание из list (одномерный массив)

print(arr) # [1 2 3 4 5]
print(arr.shape) # (5,)
print(arr.dtype) # int64
print(arr.ndim) # 1, т.к. одномерный массив

print("\n")

'''
2-ой способ создания массива
'''
arr2 = np.array([1, 2, 3, 4, 5]) # создание из list (одномерный массив)

print(arr2) # [1 2 3 4 5]
print(arr2.shape) # (5,)
print(arr2.dtype) # int64
print(arr2.ndim) # 1, т.к. одномерный массив

print("\n")

'''
задаем тип данных явно
'''
arr3 = np.array([1, 2, 3, 4, 5], dtype=np.float64)
print(arr3) # [1 2 3 4 5]
print(arr3.shape) # (5,)
print(arr3.dtype) # float64
print(arr3.ndim) 
print(len(arr3)) # 5
print(arr3.size) # 5

print("\n")

'''
приведение всех элементов к типу int64
'''
arr3 = arr3.astype(np.int64)
print(arr3) # [1 2 3 4 5]
print(arr3.dtype) # int64

print("\n")

'''Функции для заполнения массива'''
'''
1. arange, для создания одномерного массива данных, но в отличие от python range, принимает дробные значения
'''
arr4 = np.arange(0, 20, 1.5)
print(arr4) # [ 0.   1.5  3.   4.5  6.   7.5  9.  10.5 12.  13.5 15.  16.5 18.  19.5]

print("\n")

'''
2. linspace, для создания одномерного массива данных, где мы указываем диапазон и сколько значений нужно положить в массив
'''
arr5 = np.linspace(0, 5, 5) #
print(arr5) # [0.   1.25 2.5  3.75 5.  ]

arr5_2 = np.linspace(0, 2, 50)
print(arr5_2)

print("\n")

'''
3. random – заполнение массива случ.числами
'''
random_arr = np.random.random((5,))
print(random_arr) # [0.87093406 0.39985045 0.89068703 0.47501869 0.66807838]

print("\n")

'''диапазон случайных числе от [a,b]: (b-a)*np.random() + a, где b > a'''
random_arr3 = (10 - -5) * np.random.random((5,)) - 5
print(random_arr3) # [ 7.25055564  3.36457176  7.28356424 -1.57169615  6.64669952]

print("\n")

'''randint – заполнение массива числами int'''
randint_arr = np.random.randint(-5, 10, 10)
print(randint_arr) # [-5  5  5 -5  9 -1  6 -5 -2 -4]

print("\n")

'''Математические операции'''
print("Математические операции")
arr6 = np.array([1, 2, 3, 4, 5])

arr6 = np.sqrt(arr6) # квадратный корень
print(arr6)

arr6 = np.sin(arr6)
print(arr6) # 

arr6 = np.cos(arr6)
print(arr6)

arr6 = np.log(arr6)
print(arr6)

arr6 = np.exp(arr6) # 
print(arr6)

print("\n")

a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])
print(a) 
print(b)
c = a + b # np.add(a, b)
print(c) # [ 7  9 11 13 15]

c_multiply = a * b # np.multiply(a, b)
print(c_multiply) # [ 6 14 24 36 50]

c_subtract = a - b # np.subtract(a, b)
print(c_subtract) # [-5 -5 -5 -5 -5]

c_divide = a / b # np.divide(a, b)
print(c_divide) # [0.16666667 0.28571429 0.375      0.44444444 0.5       ]

print("\n")

arr7 = np.array([1, 2, 3, 4, 5])

arr7 = arr7 * 2 # множим все эл-ты массива на 2
print(arr7) # [ 2  4  6  8 10]

arr7 = arr7 ** 2 # возводим все эл-ты массива в квадрат
print(arr7) # [  4  16  36  64 100]

print("\n")

'''Функции агрегаты'''
randint_arr = np.random.randint(-5, 10, 10)
print(randint_arr) # [-5  2  7  1  7 -1 -2  8  6  3]
print(randint_arr.max()) # 8
print(randint_arr.min()) # -5
print(randint_arr.mean()) # 2.6
print(randint_arr.sum()) # 26
print(randint_arr.std()) # 4.17612260356422
print(np.median(randint_arr)) # 2.5
print(randint_arr < 2) # [True, False, False, Tue, False, True, True, False, False, False]

print("\n")

print("Манипуляции с массивами")
arr8 = np.array([5, 2, 1, 3, 4])

arr8 = np.insert(arr8, 2, -20) # вставить -20 в позицию 2
print(arr8) # [  1   2 -20   3   4   5]

arr8 = np.delete(arr8, 2) # удалить эл-т во 2-ой позиции, с матрицами можно указывать строки/столбцы
print(arr8) # [  1   2   3   4   5]

arr8 = np.sort(arr8)
print(arr8) # [1 2 3 4 5]

arr8 = np.array_split(arr8, 2)
print(arr8) # [array([1, 2, 3]), array([4, 5])]

print("\n")

print("Индексы и одномерные массивы")
arr9 = np.array([1, -2, 3, -4, 5])
arr9[0] = 0
print(arr9[2]) # 3
print(arr9[0:2]) # [ 0 -2]
print(arr9[::-1]) # [ 5 -4  3 -2  0]
print(arr9[(arr9 < 2) & (arr9 > 0)]) # []
print(arr9[(arr9 > 2) | (arr9 < 0)]) # [-2  3 -4  5]
arr9[1:4] = 0
print(arr9) # [0 0 0 0 5]

print("\n")

print("Матрицы и многомерные массивы")
matrix = np.array([(1,2,3),(4,5,6)], dtype=np.float64)
print(matrix) 
print("\n")

matrix = np.array([(1,2,3), (4,5,6), (7, 8, 9)])
print(matrix)
print("\n")

a_3d_array = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
print(a_3d_array)

matrix = np.array([(1,2,3), (4,5,6), (7, 8, 9)])
print(matrix.shape) # (3, 3)
print(matrix.ndim) # 2, т.к. двумерный массив
print(matrix.size) # 9




