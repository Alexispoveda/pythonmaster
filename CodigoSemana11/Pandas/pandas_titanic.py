#https://sites.google.com/site/aslugsguidetopython/data-analysis/pandas/pandas-example

import numpy as np
import matplotlib as p
import pdb
from pandas import *

data = read_csv('train.csv')
print(data )
print(data.columns )

men = data[data.Sex == 'male']
women = data[data.Sex =='female']
print(men  )
print(women )
proportion_women_survived = float(sum(women.SibSp))/len(women)
proportion_men_survived = float(sum(men.SibSp))/len(men)
  
print(proportion_women_survived )
print(proportion_men_survived )

print(data.Age )
print(men.Age )
print(women.Age )
print(data.columns )
print(data.xs(3) )
#
X=data['prediction']=0
print(data.columns )

print(X )
print( data.prediction[data.Sex == 'female']  )
print(data )
data.to_csv('genderbasedmodelpy.csv', index=False)






