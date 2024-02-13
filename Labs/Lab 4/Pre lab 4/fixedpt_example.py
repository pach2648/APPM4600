# import libraries
import numpy as np
    
def driver():

# test functions 
     f1 = lambda x: 1+0.5*np.sin(x)
# fixed point is alpha1 = 1.4987....

     f2 = lambda x: 3+2*np.sin(x)
#fixed point is alpha2 = 3.09... 

     Nmax = 100
     tol = 1e-6

# test f1 '''
     x0 = 0.0
     [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
     print('the approximate fixed point is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)
    
#test f2 '''
     x0 = 0.0
     [xstar,ier] = fixedpt(f2,x0,tol,Nmax)
     print('the approximate fixed point is:',xstar)
     print('f2(xstar):',f2(xstar))
     print('Error message reads:',ier)



# define routines
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    x_approx = np.zeros((Nmax + 1, 1))
    x_approx[0] = x0 #Include the initial guess
    
    while (count <Nmax):
       count = count +1
       x1 = f(x0)
       x_approx[count] = x1 #The vector of approximation
       
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [x_approx[:count],ier]
       x0 = x1

    xstar = x1
    ier = 1
    # return vector
    return [x_approx, ier]    

driver()
