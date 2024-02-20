# import libraries
import numpy as np

def driver():

# use routines    
    f = lambda x: np.e**(x**2+7*x-30)-1
    dfdx = lambda x: (2*x +7)*np.e**(x**2+7*x-30)#1st derivative of f
    d2fdx2 = lambda x: (2*x +7)*(2*x+7)*np.e**(x**2+7*x-30)+(2)*np.e**(x**2+7*x-30) #2nd derivative of f
    a = 2
    b = 4.5
    Nmax = 100
    tol = 1e-7

    # Bisection with [a,b] = [2,4.5]
    print('The Bisection with [a,b] = [2,4.5]')
    [astar,ier, count] = normal_bisection(f,a,b,tol)
    print('-the approximate root from bisection is',astar)
    print('-the error message reads:',ier)
    print('-the number of iteration of bisection is', count)
    print('\n')

    # Newton's method with x_0 = 4.5
    print("The Newton's method with initial guess = 4.5")
    x_0 = 4.5
    [p,pstar,info,it] = newton(f,dfdx,x_0,tol,Nmax)
    print("-the approximate root from Newtons's is",astar)
    print('-the error message reads:',info)
    print("-the number of iteration of Newton's is", it)
    print('\n')

    # Hybrid method
    # Find the initial guess from bisection
    print('The Hybrid method')
    [p2,pstar2,info2,it2] = hybrid(f,dfdx,d2fdx2,a,b,tol,Nmax)
    print('-the approximate root from hybrid is', '%16.16e' %pstar2)
    print('-the error message reads:',info2)
    print('-the number of iteration of hybrid is', it2)

######################################################
# define routines (I have 4 subroutines to use in this code)
######################################################
# Newton's method from class
def newton(f,fp,p0,tol,Nmax):
    """
    Newton iteration.

    Inputs:
    f,fp - function and derivative
    p0   - initial guess for root
    tol  - iteration stops when p_n,p_{n+1} are within tol
    Nmax - max number of iterations
    Returns:
    p     - an array of the iterates
    pstar - the last iterate
    info  - success message
          - 0 if we met tol
          - 1 if we hit Nmax iterations (fail)
     
    """
    p = np.zeros(Nmax+1);
    p[0] = p0
    for it in range(Nmax):
      p1 = p0-f(p0)/fp(p0)
      p[it+1] = p1
      if (abs(p1-p0) < tol):
          pstar = p1
          info = 0
          return [p,pstar,info,it]
      p0 = p1
    pstar = p1
    info = 1
    return [p,pstar,info,it]

# Find the Newton basin of convergence
def bisection_newton_basin_of_conv(f,dfdx,d2fdx2,a,b,tol):
    
    #    Inputs:
    #     f,a,b       - function and endpoints of initial interval
    #     dfdx, d2fdx2    - first and second derivative of the function f
    #      tol        - bisection stops when interval length < tol

    #    Returns:
    #      astar - approximation of root
    #      ier   - error message
    #            - ier = 1 => Failed
    #            - ier = 0 == success

    #     first verify there is a root we can find in the interval 

    fa = f(a)
    fb = f(b);
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier, count]

    #   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier, count]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier, count]

    d = 0.5*(a+b)
    count = 0
    while (abs(d-a)> tol):
      fd = f(d)
      dfd_dx = dfdx(d)
      d2fd_dx2 = d2fdx2(d)
      
      if (abs((fd*d2fd_dx2)/(dfd_dx)**2) < 1):
        astar = d
        ier = 0
        return [astar, ier, count]
      
      if (fd ==0):
        astar = d
        ier = 0
        return [astar, ier, count]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      count = count +1
    #      print('abs(d-a) = ', abs(d-a))
      
    astar = d
    ier = 0
    return [astar, ier, count]

# Hybrid method
def hybrid(f,dfdx,d2fdx2,a,b,tol,Nmax):
    # Find the initial guess from bisection
    [astar,ier, count] = bisection_newton_basin_of_conv(f,dfdx,d2fdx2,a,b,tol)
    # Use the initial guess from bisection
    [p,pstar,info,it] = newton(f,dfdx,astar,tol,Nmax)
    return [p,pstar,info,it]

# Bisection method from class
def normal_bisection(f,a,b,tol):
    
    #    Inputs:
    #     f,a,b       - function and endpoints of initial interval
    #      tol  - bisection stops when interval length < tol

    #    Returns:
    #      astar - approximation of root
    #      ier   - error message
    #            - ier = 1 => Failed
    #            - ier = 0 == success

    #     first verify there is a root we can find in the interval 

    fa = f(a)
    fb = f(b);
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier, count]

    #   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier, count]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier, count]

    count = 0
    d = 0.5*(a+b)
    while (abs(d-a)> tol):
      fd = f(d)
      if (fd ==0):
        astar = d
        ier = 0
        return [astar, ier, count]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      count = count +1
    #      print('abs(d-a) = ', abs(d-a))
      
    astar = d
    ier = 0
    return [astar, ier, count]
      
driver()               

