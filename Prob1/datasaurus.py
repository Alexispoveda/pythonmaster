import matplotlib.pyplot as plt
import numpy as np
import csv

#imagenes = ['dino', 'away', 'h_lines', 'v_lines', 'x_shape', 'star', 'high_lines', 'dots']
imagenes = []
Dicimagenes = {}

with open('Prob1\problema1\DatasaurusDozen.tsv', 'r') as f:
    reader = csv.reader(f, delimiter='\t') 
    for row in reader:
        if row[0] not in imagenes:
            imagenes.append(row[0])
    imagenes = imagenes[1:] 


for elem in imagenes:
    listaP = []
    with open('Prob1\problema1\DatasaurusDozen.tsv', 'r') as f:
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

plt.scatter(x,y)

plt.show()

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
    plt.scatter(x,y)

plt.show()