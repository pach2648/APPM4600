import numpy as np
import numpy.linalg as la
import math

def driver():

    mat1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
    vec1 = np.array([10,11,12]) #only vector (column = 1 only!!)

    mv = matVecMulti(mat1,vec1)

    print("Matrix:")
    print(mat1)
    print("\nVector:")
    print(vec1)
    
    print("\nThe dot product is : ", mv)

    print("The dot product using 'dot()' is : ", mat1.dot(vec1))

    return

def matVecMulti(matrix,vector):
    # Check if the size of column is equal to the length of vector
    if len(matrix) != len(vector):
        print("Cannot calculate because incompatible matrix and vector dimensions for multiplication")

    # Create matrix with zeros inside
    result = np.zeros(len(matrix[0]))
    # Rows
    for i in range(len(matrix)):
        # Columns
        for j in range(len(matrix[0])): 
            result[i] = result[i] + matrix[i,j] * vector[j]

    return result
driver()
