########################################################################
# This python script presents examples of numpy array creation and manipulation
# APPM 4650 Fall 2021
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

# Here is an example of a 3D array (tensor) of size 2 x 2 x 3
#print("3D array T (tensor)");
#T = np.array([[[1,2,0],[3,4,-1]],[[5,6,-2],[7,8,-3]]]);
#print(T)
#print("T is of dimension %d" % T.ndim) #number of dimensions (3)
#print("T is an array of shape");
#print(T.shape) #shape is 2 x 2 x 3
#print("T has length %d" % len(T)) #length is 2
#print("T[1] returns a 2D array (matrix)");
#print(T[1]) # matrix 1, or T[1,:,:]
#print("T[1,1] returns a 1D array (vector)");
#print(T[1,1]) #row 1 of matrix 1, or T[1,1,:]
#print("T[1,1,2] returns the corresponding entry")
#print(T[1,1,2]) #entry 2 of row 1 of matrix 1

input(); #pause until key is pressed

# Checking data type in an array
print("Comparing data types of [1,2,3] and [1.,2.,3.]")
intarr = np.array([1,2,3]);
print(intarr.dtype);
fltarr = np.array([1.,2.,3.]);
print(fltarr.dtype);

# You can specify the data type in the definition, but default is float.
# You can define numpy arrays of int,float,complex,bool,strings,etc.

input(); #pause until key is pressed
########################################################################
# Commonly used functions to create arrays
print("Commonly used functions to create arrays");

print("arange(n)");
nrng = np.arange(10);
print(nrng); #same as range, but with numpy!

print("linspace(a,b,n)");
nlin = np.linspace(0,1,6); #6 equispaced points between 0 and 1 (Matlab users deja vu)
print(nlin);

print("ones(shape)");
n_ones = np.ones((2,4)); #array of ones of the prescribed shape
print(n_ones);
print("zeros(shape)");
n_zeros = np.zeros((3,3)); #array of zeros of prescribed shape
print(n_ones);
print("eye(n)");
idmat = np.eye(4); #identity matrix
print(idmat);
print("diag(array1D)");
dgmat=np.diag(a); #diagonal matrix with values in vector a
print(dgmat);

input(); #pause until key is pressed
######################################################################
# Indexing, slicing, fancy indexing (with boolean or integer containers)

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

print("slices of matrix M");
M = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]]);
print(M);
print("M[::2] = ");
print(M[::2])
print("M[:,::2] = ");
print(M[:,::2])
print("M[::2,1::2] = ");
print(M[::2,1::2])

#print("slices of tensor T");
#T = np.array([[[1,2,0],[3,4,-1]],[[5,6,-2],[7,8,-3]]]);
#print("T[:,:,::2] = ");
#print(T[:,:,::2])

input(); #pause execution until key press

print("-------------Fancy indexing examples------------------");
# 'Fancy' indexing: we don't always want to access entries or sub-arrays using
# constant strides and such. Python (and other languages) allows us to access
# these using boolean arrays (returning only entries corresponding to True) or
# integer lists

print("We generate a list of 15 random integers from 0 to 20");
# This generates a list of 15 random integers from 0 to 20
np.random.seed(3);
arand = np.random.randint(0, 21, 15);
print(arand);

print("Extract multiples of 3 using boolean indices");
# Boolean indices are extremely useful to automatically extract or modify entries:
# Let's extract which ones are multiples of 3 (are 0 mod 3)
mult3 = (arand % 3 == 0);
print(mult3); #array of booleans
arand_m3 = arand[mult3];
print(arand_m3); #this extracts a numpy array of elements for which mult3[i]==True

print("Use boolean indexing to double all odd entries and zero out all even ones");
# We can use these indices to change entries which satisfy a condition! For example,
# multiplying all odd entries by 2 and setting all even to 0
odd = (arand % 2 == 1);
even = (arand % 2 == 0);
arand[odd] = 2*arand[odd];
arand[even] = 0;
print(arand)

# Arrays of integers can be used as indices to extract submatrices, define new
# arrays and modify array entries. This can be done in any of the dimensions of
# the array (same as with slicing)
print("We generate a random 5 x 5 matrix with entries in (0,1)");
Mrand = np.random.rand(5,5); #random 5 x 5 matrix, uniform(0,1)
print(Mrand);

print("Mrand[[0,1,3]] = ")
rowidx =[0,1,3];
print(Mrand[rowidx]);
colidx = [1,2,4];
print("Mrand[[0,1,3],[1,2,4]] = ")
print(Mrand[rowidx,colidx])
print("Note that this produces a list of entries, not a submatrix (like slicing does)");
print("Mrand[:,[1,2,4]] = ")
print(Mrand[:,colidx])
print("Note that this produces a submatrix");

input();

################################################################################
# Basic operations on arrays
# The default for most basic array operations is to carry them out elementwise.
# these operations are much more efficient than in native python.
print("-------------numpy array operations examples--------------------\n");

a = np.array([1,2,3,4]);
print(a);
print("adding a scalar to vector a")
print(a + 1.5);
print("adding two vectors")
print("b = ")
b = np.array([-2,10,7,4]);
print(a+b);
print("multiplying an array by scalar 2*a =");
print(2*a)
print("exponentiation 2^a = ")
print(2**a)
print("Note product of two vectors is elemenwise, not dot / matrix multiplication, a*b=")
print(a*b)
print("to carry out dot product / mat mult, use @ or dot, a.dot(b)=")
print(a @ b)
print(a.dot(b))

print("we can also compare arrays elementwise. For example, a>b = ")
print(a>b)

# Reductions / other operations on arrays (sum, cumsum, min, max)
print("sum(b) = %d" % np.sum(b));
print("max(b) = %d" % np.max(b));
print("max(b) = %d" % np.min(b));

# These functions can also be called as b.sum(), b.max(), b.min() (attributes of
# the class of numpy arrays)

print("sum of entries of a matrix along different dims");
M = np.array([[1,2,3],[4,5,6],[7,8,9]]);
print(M);
print("sum of M along rows");
print(M.sum(axis=0));
print("sum of M along cols")
print(M.sum(axis=1));

# There are many more array operations we will discuss as we need them in the course
# for example, transpose, flattening, reshaping, permuting dimensions, matrix operations, etc. 
