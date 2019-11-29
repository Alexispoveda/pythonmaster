import numpy as np
import matplotlib.pyplot as plt

#x = np.zeros( (5,5)  )
#print(x 
#
#y = np.random.random( ( 10, 10)  )
#print(y 
#
a=np.array( [] )
aa=[]

print(a,aa)
print(type(a))
print(a.dtype)
print(type(aa))
 
a=np.array( [1,2,3,4,5,6] )
print(a)

print(a.reshape( (6,1) ))
print(100*a)
print(100*a.reshape( (2,3) ))

print(range(1,10,1))
print(np.arange(10))

A=np.random.random( (10,10) )
print(A)
plt.figure()
plt.gray()
plt.imshow(A)
plt.show