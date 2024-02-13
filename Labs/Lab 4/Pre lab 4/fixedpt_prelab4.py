# import libraries
import numpy as np
    
def driver():

    # test functions 
    f1 = lambda x: (10/(x+4))**(0.5)
    # fixed point is alpha1 = 1.3652300134140976
    Nmax = 1000
    tol = 1e-10

    # test f1
    p0 = 1.5 # initial guess
    [p_approx,ier] = fixedpt(f1,p0,tol,Nmax)
    print('Error message reads:',ier)
    print('The approximate fixed point is:',p_approx)
    print('The number of iteration is:', len(p_approx)-1) # -1 since we don't include the p0

    # Order of convergence
    p = 1.3652300134140976
    alpha = 1
    ratios = np.abs(p_approx[1:] - p) / np.abs(p_approx[:-1] - p)**alpha
    print(ratios)

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

#def aitken(pn):
#    for i in range(len(pn)-2):
#        pn_new = pn[i]-((pn[i+1]-pn[i])**2/(pn[i+2]-2*pn[i+1]+pn))
#        
#    return

driver()
