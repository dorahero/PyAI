import numpy as np

# a = np.array([1, 2, 3])
# print(a)
# print(a.ndim)
# print(a.shape)
# print(a.size)
# print(a.dtype)
#
# b = np.array([[1, 2, 3], [4, 5, 6]])
#
# dt = np.dtype('f2')
# print(dt)
#
# people = np.dtype([('name', 'S20'), ('height', 'i4'), ('weight', 'f2')])
#
# a = np.array([('amy', 156, 50)], dtype=people)
#
# print(a)
# print(a['name'])


# a = np.arange(12)
# print(a)


# # 等比數列
# c = np.logspace(0, 9, 4, base=2, dtype='i4')
# print(c)

# 共用 memory
a = np.arange(7)
c = a.copy()
b = a[2:6]
print(a, b)
b[1] = 99
print(a, b)
print(c)

