import numpy as np

A=np.zeros( (5,5) ) 
B=np.random.random( (3,3) ) 
print(A)
print(B)

C=np.array([])
print(C)

C=np.array([1,2,3,4,5,6])
print(C)
print(C[4])

D=C.reshape( (2,3) )
print(D)

D=C.reshape( (3,2) )
print(D)
#
#print 10*D+4
#
#x=np.arange(9)
#print x

print(D)
print(D.T)



