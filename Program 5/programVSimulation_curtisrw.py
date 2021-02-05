# Curt Wilson
# CS355_Program IV 
# 04/02/2019

# Using the Rejection Method described in class write a program to generate random variables X with distribution determined
# by the density function f(x) = 1/3 (x-1)2 on the interval [0,3].

# Write a subroutine that implements the following algorithm:

# Let a=0, b=3.
# Let c =  the maximum value of f(x) over [0,3].
# Generate standard uniform random variables. a<= x <= b, 0<= y <= c
# If f(x) < y, reject the point (x,y) and repeat 3
# If y <= f(x), return X as the desired random variable.
# Call it at least 10,000 times. Make a table of values 0, 0.1, 0.2, ... 2.8, 2.9 and keep a running tally of the number of 
# variables that fall within each interval.

# At the end of the program, print out a histogram showing how the values accumulated. It should look like the graph presented in class.


import random, math, numpy as np, matplotlib.pyplot as plt

randVar = []
a = 0
b = 3

def rejection(x):
    userFunc = (1/3)*math.pow((x-1),2)
    return userFunc

c = rejection(b)

def simulateRuns():
    countx = 0
    county = 0
    countr = 0
    for i in range(10000):
        
        x = random.uniform(a, b)
        y = random.uniform(a, c)

        if a<= x <= b:
            countx = countx + 1
        if 0<= y <= c:
            county = county + 1

        if (rejection(x) < y):
            countr = countr + 1
            continue     # skips the current iteration inside the loop only
        randVar.append(x)

    
    print("X Count: ", countx)
    print("Y Count: ", county)
    print("Rejection Count: ", countr)

simulateRuns()

##############################
###  Making the histogram  ###
##############################

plt.grid = True
plt.hist([randVar], bins = 'auto', color='#0504aa', alpha=0.7, rwidth=0.85)
plt.title('Program V Histogram')
plt.xlabel('x-values')
plt.ylabel('y-values')
plt.show()
# pseudoRand = np.randn()
# x = 0,1,2,3
# randx = np.random.choice(x)
