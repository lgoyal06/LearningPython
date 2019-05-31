import numpy as np
x1= np.array([[[-1,1],[-2,2]],[[-3, 3], [-4, 4]],[[-3, 3], [-4, 4]]])
print(x1.ndim)
print(x1.shape)
print(x1.size)
x2 = np.ones(shape=(3,2,2))
print(x2)
arrayDiag = np.eye(4,4,1)
print(arrayDiag)
print(arrayDiag.shape)
print(arrayDiag.ndim)

x4 = np.array(np.random.rand(4,4)) # 2 random numbers between 0 and 1
print(x4)

