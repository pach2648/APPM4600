import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

def driver():


    f = lambda x: 1 / (1 + (10*x)**2)

    #N = 17
    N = 2
    ''' interval'''
    a = -1
    b = 1
   
   
    ''' create equispaced interpolation nodes'''
    xint = np.linspace(a,b,N+1)
    
    ''' create interpolation data'''
    yint = f(xint)
    
    ''' create points for evaluating the Lagrange interpolating polynomial'''
    Neval = 1000
    xeval = np.linspace(a,b,Neval+1)
    
    yeval_mono = np.zeros(Neval+1)
    yeval_l= np.zeros(Neval+1)
    yeval_dd = np.zeros(Neval+1)

    # Monomial expansion
    coeffs_mono = evalMono(f, N+1)
    yeval_mono = np.polyval(coeffs_mono[::-1], xeval) #Reverse the coefficients before passing to polyval

    # Lagrange Polynomial and Newton-Divided Differences
    '''Initialize and populate the first columns of the 
     divided difference matrix. We will pass the x vector'''
    y = np.zeros( (N+1, N+1) )
     
    for j in range(N+1):
       y[j][0]  = yint[j]

    y = dividedDiffTable(xint, y, N+1)
    ''' evaluate lagrange poly '''
    for kk in range(Neval+1):
       yeval_l[kk] = eval_lagrange(xeval[kk],xint,yint,N)
       yeval_dd[kk] = evalDDpoly(xeval[kk],xint,y,N)
          

    


    ''' create vector with exact values'''
    fex = f(xeval)
    
    plt.figure()    
    plt.plot(xeval,fex,'ro-',label='Exact Values')
    
    plt.plot(xeval,yeval_l,'bs--',label='lagrange') 
    plt.plot(xeval,yeval_dd,'c.--',label='Newton DD')
    plt.plot(xeval,yeval_mono,'ko-',label='Monomial')
    plt.legend()

    plt.figure()
    err_mono = abs(yeval_mono-fex)
    err_l = abs(yeval_l-fex)
    err_dd = abs(yeval_dd-fex)
    plt.semilogy(xeval,err_mono,'ko-',label='Monomial')
    plt.semilogy(xeval,err_l,'ro--',label='lagrange')
    plt.semilogy(xeval,err_dd,'bs--',label='Newton DD')
    
    plt.legend()
    plt.show()


def eval_lagrange(xeval,xint,yint,N):

    lj = np.ones(N+1)
    
    for count in range(N+1):
       for jj in range(N+1):
           if (jj != count):
              lj[count] = lj[count]*(xeval - xint[jj])/(xint[count]-xint[jj])

    yeval = 0.
    
    for jj in range(N+1):
       yeval = yeval + yint[jj]*lj[jj]
  
    return(yeval)
  
    


''' create divided difference matrix'''
def dividedDiffTable(x, y, n):
 
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                                     (x[j] - x[i + j]));
    return y;
    
def evalDDpoly(xval, xint,y,N):
    ''' evaluate the polynomial terms'''
    ptmp = np.zeros(N+1)
    
    ptmp[0] = 1.
    for j in range(N):
      ptmp[j+1] = ptmp[j]*(xval-xint[j])
     
    '''evaluate the divided difference polynomial'''
    yeval = 0.
    for j in range(N+1):
       yeval = yeval + y[0][j]*ptmp[j]  

    return yeval

def evalMono(f, N):
    h = 2 / (N-1)
    x_nodes = np.array([-1 + (j - 1) * h for j in range(1, N + 1)])
    y_nodes = f(x_nodes)
    
    V = np.vander(x_nodes, increasing = True)
    coeff = np.linalg.solve(V, y_nodes)
    return coeff

driver()        
