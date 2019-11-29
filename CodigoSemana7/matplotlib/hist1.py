import matplotlib.pyplot as plt
import random


x=[random.random()*50.0 for i in range(50)]
print(x)


plt.figure()
plt.hist(x,bins=15)
plt.show()