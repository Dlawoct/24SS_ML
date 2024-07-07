import numpy as np

a1 = np.ones((2, 3))
a2 = np.zeros((2, 2))
#print(np.hstack([a1, a2])) #hstack은 행의 수가 같은 배열을 옆으로 연결하는 형식

b1 = np.ones((2, 3))
b2 = np.zeros((3, 3))
#print(np.vstack([b1, b2])) #vstack은 열의 수가 같은 배열을 위아래로 연결하는 형식


#연습 문제 3.2.1
a = np.zeros((3,3))
b = np.ones((3,2))
c = np.hstack([a,b])
print(c)

d = np.arange(10,160,10)
e = d.reshape(3,5)
print(e)

f = np.vstack([c,e])
print(np.vstack([f,f]))



