import numpy as np

a = np.array([[4,  3,  5,  7],
              [1, 12, 11,  9],
              [2, 15,  1, 14]])

print(np.sort(a))  # 기본이 axis=1 과 동일(행 정렬)
print(np.sort(a, axis=0)) # 열 정렬

b = np.array([42, 38, 12, 25])
j = np.argsort(b) #순서만 알고싶으면 argsort
print(j)
print(b[j])


#연습 문제 3.3.2

x = np.array([[  1,    2,    3,    4],
              [ 46,   99,  100,   71],
              [ 81,   59,   90,  100]])

h = np.argsort(x[1,:])
print(x[:,h])