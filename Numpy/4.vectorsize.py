# 배열의 차원과 크기 알아내기
# ndim 속성은 배열의 차원, shape 속성은 배열의 크기 반환
import numpy as np

a = np.array([1, 2, 3])
print(a.ndim)
print(a.shape)

c = np.array([[0, 1, 2], 
              [3, 4, 5]])
print(c.ndim)
print(c.shape)