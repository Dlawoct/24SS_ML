import numpy as np

#dtype은 배열의 자료형에 사용됨
x = np.array([1, 2, 3])
print(x.dtype)

y = np.array([1, 2, 3], dtype='f')
print(y.dtype)
print(y[0] + y[1])

print(np.array([0, 1, -1, 0]) / np.array([1, 0, 0, 0]))
#inf는 무한대, nan은 정의 할 수 없는 숫자