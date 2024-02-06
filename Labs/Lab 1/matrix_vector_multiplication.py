import numpy as np
import numpy.linalg as la
import math
import time

def driver():

    # Create a 3x3 matrix
    mat1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
    # Create a 3x1 vector
    vec1 = np.array([10,11,12]) #only vector (column = 1 only!!)
    # Find the multiplication of the matrix and vector above
    mv = matVecMulti(mat1,vec1)

    # Print all the results
    print("Matrix:")
    print(mat1)
    print("\nVector:")
    print(vec1)   
    print("\nThe dot product is : ", mv)
    
    # Check with built-in function in Numpy
    # If the dimension of column is not equal to the length of vector,...
    # ... do not use dot()
    if len(mat1) == len(vec1):
        print("The dot product using 'dot()' is : ", mat1.dot(vec1))
        print("The dot product using 'np.matmul()' is : ", np.matmul(mat1, vec1))
    
########################################################
    # Test with bigger matrix and vector
    a = np.random.random( (100,100) )
    b = np.random.rand(100)

    start = time.time()
    mv2 = matVecMulti(a,b)
    end = time.time()
    print("The time of execution of above program is :",(end-start) * 10**3, "ms")

    start = time.time()
    mv2 = a.dot(b)
    end = time.time()
    print("The time of execution of above program is :",(end-start) * 10**3, "ms")

    return

# My code to find matrix vector multiplication
def matVecMulti(matrix,vector):
    # Check if the dimension of column is equal to the length of vector
    if len(matrix) != len(vector):
        print("Cannot find the result \nsince incompatible matrix and vector "
              "dimensions for multiplication")
    else:
        # Create matrix with zeros inside
        result = np.zeros(len(matrix[0]))
        # Rows
        for i in range(len(matrix)):
            # Columns
            for j in range(len(matrix[0])): 
                result[i] = result[i] + matrix[i,j] * vector[j]

        return result
driver()
