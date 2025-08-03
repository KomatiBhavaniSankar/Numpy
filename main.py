import numpy as np
'''
a_mul = np.array([[1,2,3],
[4,5,6],
[7,8,9]

])

print(a_mul)

print(a_mul.ndim)
print(a_mul.size)
print(a_mul.dtype)



print(a_mul[0])
print(a_mul[0,1])
print(a_mul[1])
print(a_mul.shape)


d = {'1':'A'}


#a = np.array([[1,2,3],[4,"hello",5],[6,7,8]

a = np.array([[1,2,3],[4,d,5],[6,7,"hello"]

])

print(a.dtype)
print(type(a[2][2]))

a = np.full((2,10,4), 9 )
print(a)

a = np.zeros((10,5,4))
print(a)

a = np.ones((10,5,4))
print(a)


a = np.empty((10,5,4))
print(a)


x_values =  np.arange(0,1000,5)
print(x_values)

x_values = np.linspace(0,100,1001)
print(x_values)


print(np.nan)
print(np.inf)
print(np.isnan(np.nan))
print(np.isinf(np.inf))
'''
l1 = [1,2,3,4,5]
l2=[6,7,8,9,0]

a1 = np.array(l1)
a2 = np.array(l2)

print(l1*5)
print(a1*5)