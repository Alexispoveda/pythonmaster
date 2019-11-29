import matplotlib.pyplot as plt
import numpy as np
import csv

def leyenda(x,y):
    correl = np.corrcoef(x,y)
    r = correl[0][1]

    return '''
    Media de x: {0:.3f}
    Media de y: {1:.3f}
    Varianza de x: {2:.3f}
    Varianza de y: {3:.3f}
    Correlacion de X e Y: {4:.3f}'''.format(np.mean(x),np.mean(y),np.std(x),np.std(y),r)

color = [
    'sienna',
    'tan',
    'gold',
    'navy', 
    'plum', 
    'maroon', 
    'coral',
    'olive', 
    'salmon',
    'purple', 
    'tomato', 
    'teal']
imagenes = []
Dicimagenes = {}

#Laptop de Alexis
with open('/Users/alexispoveda/Desktop/Python/TareaPythonCientifico/Archivos/ArchivosTarea3/problema1/DatasaurusDozen.tsv', 'r') as f:
#Laptop de Gabo
#with open('Prob1\problema1\DatasaurusDozen.tsv', 'r') as f:
    reader = csv.reader(f, delimiter='\t') 
    for row in reader:
        if row[0] not in imagenes:
            imagenes.append(row[0])
    imagenes = imagenes[1:] 


for elem in imagenes:
    listaP = []
    #Laptop de Alexis
    with open('/Users/alexispoveda/Desktop/Python/TareaPythonCientifico/Archivos/ArchivosTarea3/problema1/DatasaurusDozen.tsv', 'r') as f:
    #Laptop de Gabo
    #with open('Prob1\problema1\DatasaurusDozen.tsv', 'r') as f:
        reader = csv.reader(f, delimiter='\t') 
        for row in reader:
            if(elem==row[0]):
                listaP.append([float(row[1]), float(row[2])])
        Dicimagenes[elem] = listaP

#Impresion del Dino    
plt.figure()

x = []
y = []
for point in Dicimagenes['dino']:
    x.append(point[0])
    y.append(point[1])
plt.scatter(x,y, color='indigo')
plt.legend([
    'Media de x: ' + str(np.mean(x)),
    'Media de y: ' + str(np.mean(y)),
    'Varianza de x: ' + str(np.std(x)),
    'Varianza de y: ' + str(np.std(y)),
    'Correlacion de x e y: ' + str(np.corrcoef(x,y))
])
plt.text(70,80, leyenda(x,y))
plt.title('Dino')
plt.xlabel('X')
plt.ylabel('Y')

del Dicimagenes['dino']

#Impresion de las demas imagenes
plt.figure()

for i, img in enumerate(Dicimagenes):
    plt.subplot(3,4,i+1)
    x = []
    y = []
    for point in Dicimagenes[img]:
        x.append(point[0])
        y.append(point[1])
    plt.scatter(x,y, color=color[i])
    plt.text(70,0, leyenda(x,y), fontsize=8)
    plt.title(img)
    plt.xlabel('X')
    plt.ylabel('Y')
plt.subplots_adjust(wspace=2, hspace=2)
plt.show()