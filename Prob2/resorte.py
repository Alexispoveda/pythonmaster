import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#Modelo
def model(x,t):
    k = 1
    b = 1
    dxdt = -(k/b)*x
    return(dxdt)

#Initial condition
x0 = 0.5

#lapso de tiempo
tNormal = np.arange(0,10, 0.1)
tMenor = np.arange(0,10, 0.001)
tMayor = np.arange(0,10,1)

#solve ODE
xNormal = odeint(model, x0, tNormal)
xMenor = odeint(model, x0, tMenor)
xMayor = odeint(model, x0, tMayor)


print('x(10) = {}'.format(xNormal[-1]))
#plot
plt.figure()

plt.subplot(3,1,1)
plt.title('Sistema Resorte Amortiguador')
plt.plot(tNormal,xNormal, color='r')
plt.legend(['dt=0.1'])
plt.text(6,0.2, 'x(10) = {}'.format(xNormal[-1]), fontsize=8)

plt.subplot(3,1,2)
plt.plot(tMenor, xMenor, color='g')
plt.legend(['dt=0.001'])

plt.subplot(3,1,3)
plt.plot(tMayor, xMayor, color='b')
plt.legend(['dt=1'])


plt.ylabel('dx/dt')
plt.xlabel('t')
plt.show()
