import pandas as pd
#matplotlib inline
import random
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame()
print df 

df['x'] = random.sample(range(1, 100), 25)
df['y'] = random.sample(range(1, 100), 25)

print df 

#sns.lmplot('x', 'y', data=df, fit_reg=False)
sns.plt.figure()


##sns.kdeplot(df.y)
##
##sns.plt.figure()
##sns.kdeplot(df.y, df.x)
##
##sns.plt.figure()
##sns.distplot(df.x)
##
##sns.plt.figure()
##plt.hist(df.x, alpha=.3)
##
##sns.plt.figure()
##sns.rugplot(df.x);
##
##sns.plt.figure()
##sns.boxplot([df.y, df.x])
###
sns.plt.figure()
sns.heatmap([df.y, df.x], annot=True, fmt="d")
#
sns.plt.figure()
sns.clustermap(df)
#
sns.plt.show()




