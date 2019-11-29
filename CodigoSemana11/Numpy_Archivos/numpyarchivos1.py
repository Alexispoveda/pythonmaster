import numpy as np

"""
Demonstrate some array calculations using NumPy.
"""

## Read a csv file as a matrix
X = np.loadtxt("simple_numpy.csv", delimiter=",")
print(X)
##
#### Print the dimensions of the array X
print("The dimensions of X are:")
print(X.shape)
##
#### Print the number of values in X that are greater than 10
print("\nThe number of entries of X that exceed 10:")
print((X > 10))
print((X > 10).sum() )
print((X > 10).sum(0) )
#
#### Print the proportion of values in X that are greater than 10
print("\nThe proportion of all entries of X that exceed 10:")
print((X > 10).mean())
##
#### Print the proportion of values in each column of X that are 
#### greater than 10
print("\nThe proportion of entries in each column of X that exceed 10:")
print((X > 10).mean(0))
#
### Select the rows whose mean is greater than 5
#rm = X.mean(1)
#print rm
#ii = np.flatnonzero(rm > 5)
#print ii
#Y = X[ii,:]
#print Y
#print "\nThe column medians of X, restricted to rows with mean exceeding 5:"
#print np.median(Y, 0)
#
### Reorder the rows of X so that the row-wise means are increasing
#rm = X.mean(1)
#ii = np.argsort(rm)
#Y = X[ii,:]
#print "\nThe first five rows of X when sorted by increasing row mean:"
#print Y[0:5,:]
#
Y = X.copy()
print(X)
w=Y.sort(0)    ## Sort within columns
print(w)

#Z = X.copy()
#Z.sort(1)    ## Sort within rows

## The proportion of the rows of X in which the second column has a 
## greater value than the first column
print("\nThe proportion of the rows of X in which the second column has\n"
      "a greater value than the first column:")
print((X[:,1] > X[:,0]).mean() )