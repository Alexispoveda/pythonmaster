import pandas as pd 
from pandas import DataFrame, read_csv
import numpy as np
import matplotlib.pyplot as plt

data=read_csv('/Users/alexispoveda/Desktop/Tarea/CodigoSemana11/Pandas/DressesDataSet.csv')
print(data.columns)
print(data.head() )
print(data.describe() )

### Question a
print(data.Rating )
rat_grt0=data[data.Rating > 0] 
print(rat_grt0.Rating)
print(np.average(rat_grt0.Rating) )
print(rat_grt0.Rating.mean() )

#### Question b
rec1=data[data.Recommendation == 1]
print(rec1)
print(rec1.Dress_ID)
count=0
print(data.Recommendation == 0)
rec0=data[data.Recommendation == 0]
print(rec0)
print(rec0.Dress_ID)


rec0pat=rec0['Pattern Type'] == "animal"
print(rec0pat)
for b in rec0pat:
  if b==True:
      count=count+1
print(count)

print(rec0pat.count() )
print(rec0pat.sum() )

##### Question c
print(data[(data['Season'] == 'Summer' ) & (data['Style'] == 'Sexy' )] )

#### Question d
pivot1= pd.pivot_table(data,index=["Price","Dress_ID"])
print("pivot1")
print(pivot1)
#
#print(data['Price']
dfcount = data.groupby('Price', as_index=True)
print(dfcount)
print(dfcount.groups)
dicts=dfcount.groups
print(dicts)
lengths = {key:len(value) for key,value in dicts.items()}
print(lengths)

#### Question e
vals=["null","microfiber","Polyester","silk","cotton"]
vals2=["S","M","L","XL","free"]

x=data.loc[data.Material.isin(vals)]
print(x )
y=x.loc[x.Size.isin(vals2)] 
print(y)
#
pivot2 = pd.pivot_table(y,index=["Material"],values=["Dress_ID"],columns="Size",aggfunc='count',margins=True)
print("")
print(pivot2 )
pivot2 = pivot2.fillna(0) 
print(pivot2)

pivot2.to_csv('/Users/alexispoveda/Desktop/Tarea/CodigoSemana11/Pandas/dresses_results.csv')



