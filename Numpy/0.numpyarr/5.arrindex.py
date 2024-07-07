#배열의 인덱싱
import numpy as np

a = np.array([0, 1, 2, 3, 4])
print(a[2], a[-1])

b = np.array([[0, 1, 2], 
              [3, 4, 5]])
print(b[0,0], b[0,1], b[1,0])

print(b[0,:])
print(b[:,1])
print(b[1, 1:])
print(b[:2,:2])

#연습문제 2
m = np.array([[ 0,  1,  2,  3,  4],
            [ 5,  6,  7,  8,  9],
            [10, 11, 12, 13, 14]])
print(m[1,2])
print(m[-1,-1])
print(m[1,1:3])
print(m[1:,2])
print(m[:2,3:])