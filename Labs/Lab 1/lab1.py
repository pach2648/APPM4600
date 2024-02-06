import numpy as np
import matplotlib.pyplot as plt

# Vectors
x = [1, 2, 3]
y = np.array([1,2,3])

print("this is 3y", 3*y)

# Plotting
X = np.linspace(0,2*np.pi,100)
Ya = np.sin(X)
Yb = np.cos(X)

#plt.plot(X, Ya)
#plt.plot(X, Yb)
#plt.show()

# label
X = np.linspace(0,2*np.pi,100)
Ya = np.sin(X)
Yb = np.cos(X)

#plt.plot(X, Ya)
#plt.plot(X, Yb)
#plt.xlabel("x")
#plt.ylabel("y")
#plt.show()

print("Size of X =",len(X))

##############################
# Exercise
x = np.linspace(1,10,10)
y = np.arange(1,11,1)

print(x)
print(y)
print("Length of x is", len(x))
print("Length of y is", len(y))

print("The first three entries of x are", x[0:3])

w = 10**(-np.linspace(1,10,10))
x = np.linspace(1,10,len(x))
print(w)
plt.semilogy(x,w,label="w")

s = 3*w
plt.semilogy(x,s,label="3w")
plt.xlabel("x")
plt.ylabel("w")
plt.title("x vs w")
plt.legend(loc='upper right');
plt.show()

exit()


