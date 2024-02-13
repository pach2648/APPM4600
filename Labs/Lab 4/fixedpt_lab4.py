# import libraries
import numpy as np
    
def driver():
######################## Pre lab 4 ########################
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
    ###order_conv = order_of_conv(p, p_approx)
    ###print('The order of convergence is:',order_conv)
    
    

########################## Lab 4 #########################
    p_hat_seq, iteration = aitken(p_approx,tol=1e-10,Nmax=100)
    print("\n")
    print("Sequence after applying Aitken's method:", p_hat_seq)
    print("The number of iteration after applying Aitken's method is:", iteration)

    alpha = order_of_conv(p_approx)
    print(alpha)
    
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

def aitken(pn,tol,Nmax):
    pn_hat_seq = np.zeros_like(pn)
    for i in range(Nmax-2):
        pn_hat_seq[i] = pn[i]-((pn[i+1]-pn[i])**2)/(pn[i+2]-2*pn[i+1]+pn[i])
        
        if abs(pn_hat_seq[i] - pn[-1] < tol):
            count = i
            break

    # Remove the last two elements since they always output zeros   
    return pn_hat_seq[:count],count

def order_of_conv(p_hat):
    alpha = np.zeros_like(p_hat)
    for i in range(2,len(p_hat)-1):
        num_log = np.log(np.abs(p_hat[i+1]-p_hat[i])/np.abs(p_hat[i]-p_hat[i-1]))
        dem_log = np.log(np.abs(p_hat[i]-p_hat[i-1])/np.abs(p_hat[i-1]-p_hat[i-2]))
        alpha[i] = num_log / dem_log
    return alpha

#def order_of_conv(pa):
#    alpha = np.zeros_like(pa)
#    for i in range(len(pa)-2):
#        alpha[i] = (np.log((pa[i+1]-pa[i])/(pa[i]-pa[i-1])))/(np.log((pa[i]-pa[i+1])/(pa[i-1]*pa[i-2])))
#
#    return alpha

driver()
