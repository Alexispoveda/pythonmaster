import matplotlib.pyplot as plt
import numpy as np

A=np.zeros( (5,5)  )
print(A)
for i in range(0,5):
    print(i)
    A[i,i]=i*30

print(A)


plt.figure()
#plt.gray()
plt.imshow(A,interpolation='nearest')
plt.show()



