import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

plt.close('all')

#Definicion de Tiempo
a = 1.1
b = 0.4
c = 0.1
d = 0.4

#Ecuaciones Simultaneas
def dP_dt(P, t):
    return [P[0]*(a - b*P[1]), -P[1]*(c - d*P[0])]

#Definicion de Tiempo (pasos de solucion de la ecuacion)
ts = np.linspace(0, 60, 500)

#Valores poblacionales iniciales (presas y predadores)
P0 = [10, 11]

#Resulucion matematica del modelo
Ps = odeint(dP_dt, P0, ts)

#Valores calculados de cada ecuacion
prey = Ps[:,0]
predators = Ps[:,1]

#Grafica de las poblaciones de presa y predadores
plt.subplot(1, 2, 1)
plt.plot(ts, prey, "r-", label="Presa")
plt.plot(ts, predators, "b-", label="Predador")
plt.xlabel("Tiempo (meses)")
plt.ylabel("Poblacion")
plt.legend();

#Grafica de poblaciones finales despues de cada paso de tiempo de la simulacion
plt.subplot(1, 2, 2)
plt.plot(prey, predators, "b.")
plt.xlabel("Presa")
plt.ylabel("Predador")
plt.title("Diagrama de Espacio de Fase");
plt.show()


