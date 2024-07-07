#벡터화 연산
import numpy as np

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

x = np.array(data)

print(2 * x)

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(2 * a + b)
print(a == 2)
print(b > 10)
print((a == 2) & (b > 10))