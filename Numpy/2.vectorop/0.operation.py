#벡터화 연산
import numpy as np

x = np.arange(1, 10001)
y = np.arange(10001, 20001)

z = x + y #벡터 덧셈 가능
print(z[:10])

a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
print(a == b) #비교 연산자 가능
print(np.all(a==b)) #모든 원소가 같은지 비교
print(a * 10) #스칼라 곱 가능(브로드캐스팅)




