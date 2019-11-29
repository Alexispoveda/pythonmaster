import matplotlib.pyplot as plt
import numpy as np

A=np.random.random( (10,10)  )
print(A*50)

plt.figure()
plt.gray()
plt.imshow(A,interpolation='nearest')
plt.show()

