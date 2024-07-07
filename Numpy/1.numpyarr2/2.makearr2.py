import numpy as np

a = np.arange(12)
b = a.reshape(3, 4) #내부 데이터는 보존한 채로 형태만 바꾸는 reshape
print(b)

print(a.reshape(2, 2, -1)) #원소의 갯수가 정해져있어 -1로 대체가 가능
print(a.reshape(2, -1, 2))

print(b.flatten(), b.ravel()) #다차원 배열을 1차원 배열로 만들 때 사용

