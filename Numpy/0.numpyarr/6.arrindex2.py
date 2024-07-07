#배열 인덱싱
import numpy as np

a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
idx = np.array([True, False, True, False, True,
               False, True, False, True, False])
print(a[idx]) #불리안 배열 인덱싱 방식, 배열안에 배열을 받을 수 있음

b = np.array([11, 22, 33, 44, 55, 66, 77, 88, 99])
idx2 = np.array([0, 2, 4, 6, 8])
print(b[idx2]) #정수 배열 인덱싱 방식

c = np.array([11, 22, 33, 44, 55, 66, 77, 88, 99])
idx3 = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2])
print(c[idx3]) #배열 인덱스가 원래 배열 크기보다 커도 됨

d = np.array([[1, 2, 3, 4], 
              [5, 6, 7, 8], 
              [9, 10, 11, 12]])
print(d[:,[True, False, False, True]])

#연습문제 3
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print(x[x % 3 == 0])
print(x[x % 4 == 1])
print(x[(x % 3 == 0) & (x % 4 == 1)])
