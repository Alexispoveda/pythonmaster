import matplotlib.pyplot as plt

X=[1,2,3,4,5]
Y=[2,4,6,8,10]

print(X, Y)

plt.figure()
plt.subplot(2,1,1)
plt.plot(X,Y,'b-')


Y2=[2,10,15,20,22]

plt.subplot(2,1,2)
plt.plot(X,Y2,'r.')

plt.xlim(-2,30)
#
plt.ylim(0,10)
#
plt.text(0,0,'El origen')
plt.axhline(2)

plt.xlabel('valores en x')
plt.ylabel('valores en Y')
plt.title('Una grafica en matplotlib')
plt.legend(['una serie'])
plt.show()

