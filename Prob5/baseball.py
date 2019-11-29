import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Prob5\problema5\Mariano.csv', sep=',', header=0)

#Encontrar el año con mas juegos cerrados
MaxYear = df['Year'][df['GF']==df['GF'].max()].values
print('El año donde MAriano cerro mas juegos fue el ' + str(MaxYear[0]))

#Diagrama de barras de Saves
saves = df['SV']
years = df['Year']
xi = list(range(len(years)))
plt.figure()
plt.bar(xi,saves,width=0.5, )
plt.xticks(xi,years)
#plt.show()


#Yankees Pages 
dfYankees = pd.read_csv('Prob5\problema5\Yankees.csv', sep=',', header=0)

minYear = df['Year'].min()
maxYear = df['Year'].max()

antes = dfYankees['PAge'][dfYankees['Year']<minYear].values
durante = dfYankees['PAge'][(dfYankees['Year']>=minYear) & (dfYankees['Year']<=maxYear) ].values
despues = dfYankees['PAge'][dfYankees['Year']>maxYear].values

box_plot_data = [antes, durante, despues]

plt.figure()
plt.boxplot(box_plot_data)
#plt.show()

#Premios
resdf = df.merge(dfYankees, left_on='Year', right_on='Year')

awards = resdf['Awards']
attendance = resdf['Attendance'].values


awardsbool = []
for elem in awards:
    if (type(elem)==float):
        awardsbool.append(0)
    else:
        awardsbool.append(1)

print('La correlacion de los premios y la asistencia se da por: ')
print(np.corrcoef(awardsbool, attendance))

#Subplots de asistnecia y ERA
añosMariano = df['Year']
ERAMariano = df['ERA+']

añosYankee = dfYankees['Year']
attYankee = dfYankees['Attendance']

plt.figure()
#Yankees attendance
plt.subplot(2,1,1)
xi = list(range(len(añosYankee)))
plt.bar(xi,attYankee,width=0.5, )
plt.xticks(xi,añosYankee)

#Marino
plt.subplot(2,1,2)
xi = list(range(len(añosMariano)))
plt.bar(xi,ERAMariano,width=0.5, )
plt.xticks(xi,añosMariano)

plt.show()



