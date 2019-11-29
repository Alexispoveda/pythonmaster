#http://nbviewer.ipython.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/01%20-%20Lesson.ipynb

import pandas as pd #this is how I usually import pandas
# from pandas import DataFrame, read_csv
import sys #only needed to determine Python version number

import numpy as np
import matplotlib.pyplot as plt

# The inital set of baby names and bith rates
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]
print( names )
print( births )

BabyDataSet = zip(names,births)
print( "" )
print(  BabyDataSet )

df = pd.DataFrame(data = list(BabyDataSet), columns=['Names', 'Births'] )
print( df )
#
### Check data type of the columns
print( df.dtypes )
print(  df['Births'].max() )
##
### Create graph
df['Births'].plot()
##
#### Maximum value in the data set
MaxValue = df['Births'].max()
###
#### Name associated with the maximum value
MaxName = df['Names'][ df['Births'] == df['Births'].max() ].values
print( MaxName )
#
print( df['Names'][4] )
#
####
#### Text to display on graph
Text = str(MaxValue) + " - " + MaxName
print( Text )
### Add text to graph
plt.annotate(Text, xy=(1, MaxValue), xytext=(1, 0), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points')
#
print( "The most popular name" )
print( df[df['Births'] == df['Births'].max()] )

#can also be used
##
plt.show()