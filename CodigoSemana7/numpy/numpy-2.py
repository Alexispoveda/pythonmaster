
import numpy as np
import matplotlib.pyplot as plt

A=np.random.random( (10,10) )
print(A)
plt.figure()
plt.gray()
plt.imshow(A)
plt.show