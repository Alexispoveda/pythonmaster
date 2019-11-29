import matplotlib.pyplot as plt
import numpy as np

A = np.zeros( (100,100,3) )

for i in range(100):
  for j in range(100):
      A[i,j,0]=1-i*0.01
      A[i,j,1]=0
      #-i*0.01
      A[i,j,2]=0
      #1-i*0.01

plt.imshow(A,interpolation='nearest')
plt.show()