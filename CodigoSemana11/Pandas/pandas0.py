import pandas as pd
import numpy as np

s=pd.Series( [1,3,5,np.nan,6,8] ) 
print( s )
print( s.sum() )
print( s.mean() )
#
data = [ ['ABC',-3.5,0.01], ['ABC',-2.3,0.12], ['DEF',-1.8,0.03],['DEF',3.7,0.01],
['DEF',-3.5,0.01], ['GHI',-3.5,0.01], ['GHI',-3.5,0.01] ]

print( data )
print( data[0] )
print( data[-1] )
#
print( data[0][1]+data[1][1]  )
#
df=pd.DataFrame(data, columns=['gene','log2','pval'])
print( df )
print( df['gene'] )
print( df['log2'].mean() )
 
print( df.columns )
print( df.index )
print( df.head(2) )
print( df.values )

print( df.describe() )

print( df['pval']< 0.05 )
