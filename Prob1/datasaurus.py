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
                listaP.append((row[1], row[2]))
        Dicimagenes[elem] = listaP
print(Dicimagenes)
    

with open('Prob1\problema1\DatasaurusDozen.tsv', 'r') as f:
    reader = csv.reader(f, delimiter='\t') 