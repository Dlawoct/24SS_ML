import numpy as np

a = np.zeros(5) #모든 값이 0인 배열 생성
print(a)
b = np.zeros((2, 3)) #튜플을 이용해서 다차원 배열도 가능
print(b)

e = np.ones((2, 3, 4), dtype="i8") #ones를 이용해 모든 값이 1인 배열 생성
print(e)

f = np.ones_like(b, dtype="f") #다른 배열과 같은 크기로 만들려면 zeros_like, ones_like 사용
print(f) #b와 같은 크기의 1로 구성된 배열 생성

g = np.empty((4, 3)) #배열만 생성하고 대충 초기화하는 empty
print(g)

print(np.arange(10)) # numpy의 range명령어
print(np.arange(3,21,2))

A = np.array([[1, 2, 3], [4, 5, 6]])
print(A)
print(A.T) # 전치 행렬