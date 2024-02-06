# import libraries
import numpy as np

# define routines (Bisection)
def bisection(f,a,b,tol,Nmax):
    '''
    Inputs:
      f,a,b       - function and endpoints of initial interval
      tol, Nmax   - bisection stops when interval length < tol
                  - or if Nmax iterations have occured
    Returns:
      astar - approximation of root
      ier   - error message
            - ier = 1 => cannot tell if there is a root in the interval
            - ier = 0 == success
            - ier = 2 => ran out of iterations
            - ier = 3 => other error ==== You can explain
    '''

    '''     first verify there is a root we can find in the interval '''
    fa = f(a); fb = f(b);
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier]

    ''' verify end point is not a root '''
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier]

    count = 0
    while (count < Nmax):
      c = 0.5*(a+b)
      fc = f(c)

      if (fc ==0):
        astar = c
        ier = 0
        return [astar, ier]

      if (fa*fc<0):
         b = c
      elif (fb*fc<0):
        a = c
        fa = fc
      else:
        astar = c
        ier = 3
        return [astar, ier]

      if (abs(b-a)<tol):
        astar = a
        ier =0
        return [astar, ier]
      
      count = count +1

    astar = a
    ier = 2
    return [astar,ier]

# define routines 2 (fixed point)
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    while (count <Nmax):
       count = count +1
       x1 = f(x0)
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier]
       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier]

# use routines
#############################################
# Problem 1
print('Problem 1')
# 1a
f = lambda x: (x**2)*(x-1)
a = 0.5
b = 2

Nmax = 100
tol = 1e-3

[astar1,ier1] = bisection(f,a,b,tol,Nmax)
print('the approximate root for 1a is',astar1)
print('the error message reads:',ier1)

# 1b
f = lambda x: (x**2)*(x-1)
a = -1
b = 0.5

Nmax = 100
tol = 1e-3

[astar2,ier2] = bisection(f,a,b,tol,Nmax)
print('the approximate root for 1b is',astar2)
print('the error message reads:',ier2)

# 1c
f = lambda x: (x**2)*(x-1)
a = -1
b = 2

Nmax = 100
tol = 1e-3

[astar3,ier3] = bisection(f,a,b,tol,Nmax)
print('the approximate root for 1c is',astar3)
print('the error message reads:',ier3)

#############################################
# Problem 2
print("")
print('Problem 2')
# 2a
f = lambda x: (x-1)*(x-3)*(x-5)
a = 0
b = 2.4

Nmax = 100
tol = 1e-5

[astar,ier] = bisection(f,a,b,tol,Nmax)
print('the approximate root for 2a is',astar)
print('the error message reads:',ier)

# 2b
f = lambda x: ((x-1)**2)*(x-3)
a = 0
b = 2

Nmax = 100
tol = 1e-5

[astar,ier] = bisection(f,a,b,tol,Nmax)
print('the approximate root for 2b is',astar)
print('the error message reads:',ier)

# 2c-1
f = lambda x: np.sin(x)
a = 0
b = 0.1

Nmax = 100
tol = 1e-5

[astar,ier] = bisection(f,a,b,tol,Nmax)
print('the approximate root for 2c part 1 is',astar)
print('the error message reads:',ier)

# 2c-2
f = lambda x: np.sin(x)
a = 0.5
b = (3*np.pi)/4

Nmax = 100
tol = 1e-5

[astar,ier] = bisection(f,a,b,tol,Nmax)
print('the approximate root for 2c part 2 is',astar)
print('the error message reads:',ier)


#############################################
# Problem 3
print("")
print('Problem 3')

# 3a

f1 = lambda x: x*(1+((7-x**5)/(x**2)))**3

Nmax = 100
tol = 1e-10

# when x0 = 1, it overflows the function
x0 = 7**(1/5) #verify that x=7^(1/5) is a fixed point for this function
[xstar,ier] = fixedpt(f1,x0,tol,Nmax)
print('the approximate fixed point for 3a is:',xstar)
print('f1(xstar):',f1(xstar))
print('Error message reads:',ier)



# 3b
f1 = lambda x: x-((x**5-7)/(x**2))

Nmax = 100
tol = 1e-10

# when x0 = 1, it overflows the function
x0 = 7**(1/5)
[xstar,ier] = fixedpt(f1,x0,tol,Nmax)
print('the approximate fixed point for 3b is:',xstar)
print('f1(xstar):',f1(xstar))
print('Error message reads:',ier)


# 3c
f1 = lambda x: x-((x**5-7)/(5*x**4))

Nmax = 100
tol = 1e-10

x0 = 1
[xstar,ier] = fixedpt(f1,x0,tol,Nmax)
print('the approximate fixed point for 3c is:',xstar)
print('f1(xstar):',f1(xstar))
print('Error message reads:',ier)

# 3d
f1 = lambda x: x-((x**5-7)/(12))

Nmax = 100
tol = 1e-10

x0 = 1
[xstar,ier] = fixedpt(f1,x0,tol,Nmax)
print('the approximate fixed point for 3d is:',xstar)
print('f1(xstar):',f1(xstar))
print('Error message reads:',ier)
