import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[2,4,6,8,10]
y1=[1,3,5,6,7]

plt.figure()

plt.plot(x,y,'.')
plt.plot(x,y1,'r-')
plt.xlabel("Valores en X")
plt.ylabel("Valores en Y")
plt.title("Mi primera grafica en Matplotlib")
plt.xlim(-2,10)
plt.ylim(-1,8)
plt.legend( ['Mi Grafica','serie 2'] )
plt.text(3,5,'Punto Especifico')
plt.axvline(3,0.25)
plt.axhline(6,0.25)

plt.show()


