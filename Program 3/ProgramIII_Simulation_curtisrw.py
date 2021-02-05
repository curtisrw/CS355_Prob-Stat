# Curt Wilson
# CS355_ProgramIII
# 3/6/2019

# Write a program to simulate traffic flow with 1000 cars. 
# Calculate the average transit time from A to P and calculate
# the standard deviation.  Run this program 10 times and compute the average 
# transit time for 100,000 cars and the standard deviation.
# Compare the 10 runs of 1000 with the one run of 10,000.

import random
import numpy as np
from math import sqrt

f = open("ProgramIII_Results_curtisrw.txt","a+")

# c.r.p.t. - city, road, prob, time 
crptMatrix = {
   'A':[('B',0.4,5),('C',0.6,6)],
   'B':[('D',0.4,4),('E',0.6,7)],
   'C':[('E',0.5,4),('F',0.5,6)],
   'D':[('G',0.4,4),('H',0.6,6)],
   'E':[('H',0.6,6),('I',0.4,4)],
   'F':[('I',0.6,4),('J',0.4,7)],
   'G':[('K',0.6,4),('L',0.4,6)],
   'H':[('K',0.4,4),('L',0.3,8),('M',0.3,8)],
   'I':[('L',0.5,6),('M',0.5,4)],
   'J':[('M',1.0,5)],
   'K':[('N',1.0,4)],
   'L':[('N',0.4,5),('O',0.6,6)],
   'M':[('O',1.0,5)],
   'N':[('P',1.0,5)],
   'O':[('P',1.0,5)],
}

def simNextTown(traversal):
   test = random.random()
   if test < crptMatrix[traversal][0][1]:
       return (crptMatrix[traversal][0][0],crptMatrix[traversal][0][2])
   else:
       return (crptMatrix[traversal][-1][0],crptMatrix[traversal][-1][2])

def simCar():
   currentPosition, end = 'A', 'P'
   timetaken = 0
   while currentPosition != end:
       nxt,cost = simNextTown(currentPosition)
       currentPosition = nxt
       modTimeTaken = np.random.uniform(0.0, 1.0) # uniformly distributed float
       for time in currentPosition:
         if modTimeTaken >= 0.5:
            timetaken += (cost + 1) # time can vary uniformly randomly one minute greater than ( + 1)
         else:
            timetaken += (cost - 1) # or less than the amount specied below ( - 1)
   return timetaken

def transitTime(array):
   s = 0.0
   s = sum(array)*1.0
   return s/len(array)

def standardDeviation(array):
   mu = transitTime(array)
   s = 0.0
   for x in array:
       s += (x-mu)**2
   return sqrt(s/len(array))

# simulating 1000 cars...
array = []
for sim in range(1000):
   array.append(simCar())
print("Simulate traffic flow with 1000 cars:")
print("Average transit time: %.3f"%(transitTime(array)))
print("Standard deviation: %.3f "%(standardDeviation(array)))
f.write("Simulate traffic flow with 1000 cars:")
f.write("\nAverage transit time: %.3f"%(transitTime(array)))
f.write("\nStandard deviation: %.3f "%(standardDeviation(array)))

array = []
for sim in range(10):
   array2 = []
   for sim in range(1000):
       array2.append(simCar())
   array.append(transitTime(array2))
print("Simulate 10 runs of 1000 cars:")
print("Average transit time: %.3f"%(transitTime(array)))
print("Standard deviation: %.3f "%(standardDeviation(array)))
f.write("\n\nSimulate 10 runs of 1000 cars:")
f.write("\nAverage transit time: %.3f"%(transitTime(array)))
f.write("\nStandard deviation: %.3f "%(standardDeviation(array)))

array = []
for sim in range(10000):
   array.append(simCar())
print("Simulate traffic flow with 10,000 cars:")
print("Average transit time: %.3f"%(transitTime(array)))
print("Standard deviation: %.3f "%(standardDeviation(array)))
f.write("\n\nSimulate traffic flow with 10,000 cars:")
f.write("\nAverage transit time: %.3f"%(transitTime(array)))
f.write("\nStandard deviation: %.3f "%(standardDeviation(array))+"\n")
f.write("------------------------------------------------------------------------------")
f.write("\n\n\n")

f.close()

#################################################################################################
#################################################################################################