import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import scipy.linalg as scila
import time
from time import perf_counter

def driver():

     ''' create  matrix for testing different ways of solving a square 
     linear system'''

     '''' N = size of system'''
     N = 1000
     print("N =", N)
 
     ''' Right hand side'''
     b = np.random.rand(N,1)
     A = np.random.rand(N,N)

     x1 = cal_lu(A,b)
     
     t1_start = time.perf_counter_ns() 
     x2 = scila.solve(A,b)
     t1_stop = time.perf_counter_ns()
     t_normal = t1_stop - t1_start
     print("Total time of normal solve [ns]:", t_normal)
     
     test = np.matmul(A,x2)
     r = la.norm(test-b)
     
     #print(r)

     ''' Create an ill-conditioned rectangular matrix '''
     N = 10
     M = 5
     A = create_rect(N,M)     
     b = np.random.rand(N,1)

     t1_start = time.perf_counter_ns() 
     x = scila.solve(A.T @ A,A.T @ b)
     t1_stop = time.perf_counter_ns()
     t_QR = t1_stop - t1_start
     print("Total time of QR solve [ns]:", t_QR)
     
def create_rect(N,M):
     ''' this subroutine creates an ill-conditioned rectangular matrix'''
     a = np.linspace(1,10,M)
     d = 10**(-a)
     
     D2 = np.zeros((N,M))
     for j in range(0,M):
        D2[j,j] = d[j]
     
     '''' create matrices needed to manufacture the low rank matrix'''
     A = np.random.rand(N,N)
     Q1, R = la.qr(A)
     test = np.matmul(Q1,R)
     A =    np.random.rand(M,M)
     Q2,R = la.qr(A)
     test = np.matmul(Q2,R)
     
     B = np.matmul(Q1,D2)
     B = np.matmul(B,Q2)
     return B     

def cal_lu(A,b):
     t1_start = time.perf_counter_ns() 
     lu, piv = scila.lu_factor(A)
     t1_stop = time.perf_counter_ns()
     t1 = t1_stop - t1_start
     print("Elapsed time (Factor) [ns]:", t1) 

     t2_start = time.perf_counter_ns()
     x = scila.lu_solve((lu, piv), b, trans = 0)
     t2_stop = time.perf_counter_ns()
     t2 = t2_stop - t2_start
     print("Elapsed time (lu_solve) [ns]:", t2)
     print("Total time of Lu_solve [ns]:", t1+t2)

     return x
  
if __name__ == '__main__':
      # run the drivers only if this is called from the command line
      driver()       
