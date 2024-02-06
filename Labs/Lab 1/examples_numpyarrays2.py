########################################################################
# This python script presents examples of numpy array creation and manipulation
# APPM 4650 Fall 2021  -- version2
########################################################################
import numpy as np; # import numpy library and call it np


print("-------------numpy array creation examples--------------------\n");
# Let's define some arrays. Remember: all numpy functions must be preceded by np.
# or python will not recognize them.

#np.array turns a list into a numpy array object. Each 'row' of the array is written
# between brackets.
print("1D array a = [0,1,2,3]");
a = np.array([0,1,2,3]);
print(a);
print("a[0] = %d" % a[0])
print("a[-1] = %d" % a[-1])


# Let's check some basic attributes of this 1D array:
print("a is of dimension %d" % a.ndim) #number of dimensions (1)
print("a is an array of shape");
print(a.shape) #shape (4 x 1, NOTE python just says 4 x blank !)
print("a has length %d" % len(a)) #length (in python, size of FIRST dimension)

input(); #pause until key is pressed


# Let's test playing with some array calls
# numpy arrays can be sliced in any of their dimensions to produce corresponding
# sub-arrays. Using the 1D,2D and 3D arrays a,M and T, what do you expect these
# instructions to output?
print("slices of vector a");
a = np.arange(10);
print(a);
print("a[::2] = ");
print(a[::2])
print("a[1:9:2] = ");
print(a[1:9:2])
# Can you come up with another way printing just the even entries?


input(); #pause until key is pressed

#Now we play with matrices (Tensors are in other version)
# 2D and higher-D examples:
# 2D arrays (matrices) are collections of rows, and so they're written in the form
# np.array([row_0,row_1,...,row_{m-1}]);
print("2D array M (matrix)");
M = np.array([[0,1,2],[3,4,5]]);
print(M);
print("M is of dimension %d" % M.ndim) #number of dimensions (2)
print("M is an array of shape");
print(M.shape) #shape is 2 x 3, notice this is a list!
print("M has length %d" % len(M)) #length is 2
print("Row 1 of M")
print(M[1]) #row_1 of the matrix (second row)
print("Entry M[0,2]")
print(M[0,2]) #entry 0,2 of the matrix

input(); #pause until key is pressed

print("slices of matrix M");
M = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]]);
print(M);
print("M[::2] = ");
print(M[::2])
print("M[:,::2] = ");
print(M[:,::2])
print("M[::2,1::2] = ");
print(M[::2,1::2])


input(); #pause until key is pressed

