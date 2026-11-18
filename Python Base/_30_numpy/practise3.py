'''Форма и объединение массивов'''
import numpy as np

a = np.arange(1, 25)
print(a.shape) # (24,)

b = a.reshape(4,6)
print(b.shape) # (4, 6)

c = a.reshape(2, 3, 4) # 2 * 3 * 4 = 24
print(c.shape) # (2, 3, 4)

d = c.reshape(24) # обратно в 1D
print(d.shape) # (24,)

e = c.reshape(4, 6) # из 3D сразу в 2D
print(e.shape) # (4, 6)

a = np.arange(1, 25).reshape(4, 6)

r = a.reshape(24)   # вид (если возможно)   -> shape (24,)
v = a.ravel()       # вид (если возможно)   -> shape (24,)
f = a.flatten()     # ВСЕГДА копия          -> shape (24,)

array_1 = np.arange(1, 17).reshape(4, 4)
array_2 = np.arange(17, 33).reshape(4, 4)
array_3 = np.arange(33, 49).reshape(4, 4)

'''
объедини несколько массивов по строкам и столбцам =>
! важно: для объединения формы должны быть совместимы по «свободным» осям

операция                        axis   shape результата   что делает
------------------------------  -----  ------------------  ---------------------
np.vstack((a, b, c))            0      (6, 2)              ставит друг под друга
np.hstack((a, b, c))            1      (2, 6)              ставит друг рядом
np.concatenate((a,b,c), axis=0) 0      (6, 2)              то же, что vstack
np.concatenate((a,b,c), axis=1) 1      (2, 6)              то же, что hstack
'''
vertically_stacked_arrays = np.vstack((array_1, array_2, array_3))
concatenated_arrays = np.concatenate((array_1, array_2, array_3), axis=0)
print(vertically_stacked_arrays == concatenated_arrays)

horizontally_stacked_arrays = np.hstack((array_1, array_2, array_3))
horizontally_concatenated_arrays = np.concatenate((array_1, array_2, array_3), axis=1)
print(horizontally_stacked_arrays == horizontally_concatenated_arrays)

print(f"\nраздели матрицу на равные части")

m = np.arange(1, 37).reshape(6, 6)
parts1 = np.split(m, 3, axis=0)
print(len(parts1))         # 3
print(parts1[0].shape)     # (2, 6)
print(parts1[1].shape)     # (2, 6)
print(parts1[2].shape)     # (2, 6)

parts2 = np.split(m, 3, axis=1)
print(len(parts2))         # 3
print(parts2[0].shape)     # (6, 2)
print(parts2[1].shape)     # (6, 2)
print(parts2[2].shape)     # (6, 2)

top, bottom = np.split(m, 2, axis=0)
print(top.shape)      # (3, 6)
print(bottom.shape)   # (3, 6)

m5 = np.arange(1, 31).reshape(5, 6)   # 5 строк

parts3 = np.array_split(m5, 2, axis=0)
print(parts3[0].shape)   # (3, 6)
print(parts3[1].shape)   # (2, 6)

parts4 = np.array_split(m5, 3, axis=0)
print([p.shape[0] for p in parts4])   # [2, 2, 1]

matrix_three = np.arange(1, 25).reshape(2, 3, 4)
print(c.shape)   # (2, 3, 4)

t1 = np.transpose(matrix_three, (0, 2, 1))
print(t1.shape)   # (2, 4, 3)

t2 = np.transpose(matrix_three, (2, 0, 1))
print(t2.shape)   # (4, 2, 3)

t3 = np.transpose(matrix_three, (2, 1, 0))
print(t3.shape)   # (4, 3, 2)

s02 = np.swapaxes(matrix_three, 0, 2)
print(s02.shape)   # (4, 3, 2)

s01 = np.swapaxes(matrix_three, 0, 1)
print(s01.shape)   # (3, 2, 4)

s12 = np.swapaxes(matrix_three, 1, 2)
print(s12.shape)   # (2, 4, 3)