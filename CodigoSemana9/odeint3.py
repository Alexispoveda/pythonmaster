from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def dy_dx(y, x):
    return x - y

xs = np.linspace(0,5,100)
y0 = 1.0  # the initial condition
ys = odeint(dy_dx, y0, xs)
ys = np.array(ys).flatten()

# Plot the numerical solution
plt.figure()
plt.rcParams.update({'font.size': 14})  
plt.xlabel("x")
plt.ylabel("y")
plt.plot(xs, ys);
plt.title('calculada con odeint')
plt.show()

plt.figure()
y_exact = xs - 1 + 2*np.exp(-xs)
y_difference = ys - y_exact
plt.plot(xs, ys, xs, y_exact, "+");
plt.title('Solucion exacta')
plt.show()

plt.figure()
y_diff = np.abs(y_exact - ys)
plt.semilogy(xs, y_diff)
plt.ylabel("Error")
plt.xlabel("x")
plt.title("Error integracion numerica");
# Note the logarithmic scale on the y-axis. 
plt.show()