
import pandas as pd
import numpy as np

data= [ ['foo', 'one', 'small', 1], ['foo', 'one', 'large', 2], ['foo', 'one', 'large', 2], ['foo', 'two', 'small', 3], 
['foo', 'two', 'small', 3], ['bar', 'one', 'large', 4], ['bar', 'one', 'small', 5], ['bar', 'two', 'small',6], ['bar', 'two', 'large',7] ]
print(data)

df=pd.DataFrame(data,columns=['A','B','C','D'])
print(df)
#
table=pd.pivot_table(df,values='D',index=['A','B'],columns=['C'],aggfunc=np.sum)
print(table)
#    
