import numpy as np

x = np.array([1, 2, 3, 4])

print(np.sum(x))
print(x.sum())
print(x.min())
print(x.max())
print(x.argmin()) #최솟값의 위치
print(x.argmax()) #최대값의 위치

y= np.array([1, 2, 3, 1])

print(y.mean()) #평균값
print(np.median(y)) #중앙값

z = np.array([[1,1],[2,2]])
print(z.sum(axis=0)) # 열 합계
print(z.sum(axis=1)) # 행 합계


#연습 문제 3.3.1
print("연습 문제 3.3.1")

ar = np.arange(30, dtype=float).reshape(5,6)
print(ar)
print(ar.max()) #전체의 최댓값
print(ar.sum(axis=1)) #각 행의 합
print(ar.max(axis=1)) #각 행의 최댓값
print(ar.mean(axis=0)) #각 열의 평균
print(ar.min(axis=0)) #각 열의 최솟값