########################################################################
# This python script presents examples of basic plots using numpy and pyplot
# APPM 4650 Fall 2021
########################################################################

import numpy as np; # import numpy library and call it np
from matplotlib import pyplot as plt; #import pyplot module and call it plt

# These exercises are not meant to be exhaustive, but to give you an idea of how
# use pyplot to produce 2D plots. We will start by defining a set x of equispaced
# points in [0,1], and a function defined on [0,1].

x = np.linspace(0,1,100);
def fun(y):
    return 2*np.sin(np.pi*y)-1;


#Most basic plot instruction is as follows:
plt.plot(x,fun(x)) #creates the plot figure
plt.show(); #necessary when executing from command line to generate the pop-up figure

input(); # pause execution until key is pressed

def fun2(y):
    return 3*np.cos(np.pi*y)-1;

plt.plot(x,fun(x)) #creates the plot figure
plt.plot(x,fun2(x)) #note that this 2nd plot is superimposed with the first (hold on in matlab)
plt.show(); #necessary when executing from command line to generate the pop-up figure

input(); # pause execution until key is pressed

#Now, we might want to edit our plot, change line width, markers, add x and y labels and so on.
plt.plot(x,fun(x),'g',linewidth=4,label="fun(x)") #first line is green, line is thicker
plt.plot(x,fun2(x),'r--',label="fun2(x)") #2nd plot is red and line is dashed
plt.xticks(np.linspace(0,1,11)); #changes x ticks (every 0.1 instead of 0.2)
plt.xlabel("x"); #sets label for x axis
plt.ylabel("f(x)"); #sets label for y axis
plt.title("test plot of fun(x) and fun2(x)"); #figure title
plt.legend(loc='upper right'); #add legend
plt.show();
