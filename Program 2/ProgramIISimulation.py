# Curt Wilson
# CS355_ProgramTwo
# 2/14/2019

'''
Write a program to simulate traffic flow with 10,000 cars.  Calculate the average transit time from A to P and calculate 
the standard deviation. Run this program 10 times and compute the average transit time for 100,000 cars and the standard 
deviation. Compare the 10 runs of 10,000 with the one run of 100,000.
'''

import random
import math

# path = [[("A","B", 5, 0.1)], [("A","C", 6, 0.9)]]
# , ("B","D", 4, 0.2), ("B","E", 7, 0.8), ("C","E", 4, 0.3), ("C","F", 6, 0.7), ("D","G", 4, 0.1), ("D","H", 6, 0.9), ("E","H", 6, 0.4), ("E","I", 4, 0.6), ("F","I", 3, 0.2), ("F","J", 7, 0.8), ("G","K", 4, 0.1), ("H","K", 4, 0.3), ("H","L", 8, 0.7), ("I","L", 6, 0.5), ("I","M", 4, 0.5), ("J","M", 5, 1.0), ("K","N", 4, 1.0), ("L","N", 5, 0.4), ("L","O", 6, 0.6), ("M","O", 5, 1.0), ("N","P", 5, 1.0), ("O","P", 5, 1.0)]
path = []

class Road:
    def __init__(self, start, end, time, probability):
        self.start = start
        self.end = end
        self.time = time
        self.probability = probability

class Vehicle:
    def __init__(self, position, travelTime = 0):
        self.position = position
        self.travelTime = travelTime
    def followingRoad(self):
        choices = []
        for x in range(len(path)):
            if path[x].start == self.position:
                choices.append(path[x])
        roadChoice = random.random()
        if (roadChoice < choices[0].probability) and (len(choices) < 2):
            self.travelTime += choices[0].time
            self.position = choices[0].end
        elif roadChoice < choices[0].probability:
            self.travelTime += choices[0].time
            self.position = choices[0].end
        else:
            self.travelTime += choices[1].time
            self.position = choices[1].end
            
path.append(Road("A","B", 5, 0.1))
path.append(Road("A","C", 6, 0.9)) 
path.append(Road("B","D", 4, 0.2)) 
path.append(Road("B","E", 7, 0.8)) 
path.append(Road("C","E", 4, 0.3)) 
path.append(Road("C","F", 6, 0.7)) 
path.append(Road("D","G", 4, 0.1)) 
path.append(Road("D","H", 6, 0.9)) 
path.append(Road("E","H", 6, 0.4)) 
path.append(Road("E","I", 4, 0.6)) 
path.append(Road("F","I", 3, 0.2)) 
path.append(Road("F","J", 7, 0.8)) 
path.append(Road("G","K", 4, 0.1)) 
path.append(Road("H","K", 4, 0.3))
path.append(Road("H","L", 8, 0.7)) 
path.append(Road("I","L", 6, 0.5))
path.append(Road("I","M", 4, 0.5)) 
path.append(Road("J","M", 5, 1)) 
path.append(Road("K","N", 4, 1)) 
path.append(Road("L","N", 5, 0.4)) 
path.append(Road("L","O", 6, 0.6)) 
path.append(Road("M","O", 5, 1)) 
path.append(Road("N","P", 5, 1)) 
path.append(Road("O","P", 5, 1))

def transitTime(array):
    count = 0
    for x in array:
        count += 1
    return count / len(array)

def standardDeviation(array):
    meanCal = transitTime(array)
    squareDiff = []
    for x in array:
        squareDiff.append((x - meanCal) ** 2)
    return math.sqrt(transitTime(squareDiff))

def createSimulation(trialCount):
    finalTime = []
    for x in range(trialCount):
        vehicle = Vehicle("A")
        while vehicle.position != "P":
            vehicle.followingRoad()
        finalTime.append(vehicle.travelTime)
    return transitTime(finalTime), standardDeviation(finalTime)


print("*****************************************************************************")
print("\nSIMULATIONS")
print("\n*****************************************************************************")
print("Simulation 1: 10,000 Vehicles... ")
tTime1, standard1 = createSimulation(10000)
print("The average time taken: " + str(tTime1))
print("Standard Deviation: " + str(standard1))
print("----------------------------------------------------------------------------")
print("Simulating 10,000 Vehicles 10 times... ")
test1 = []
test2 = []
for x in range(10):
    tTime2, standard2  = createSimulation(10000)
    test1.append(tTime2)
    test2.append(standard2)
print("The average time taken: " + str(transitTime(test1)))
print("Standard Deviation: " + str(standardDeviation(test2)))
print("----------------------------------------------------------------------------")
tTime3, standard3 = createSimulation(100000)
print("Simulating 100,000 Vehicles... ")
print("The average time taken: " + str(tTime3))
print("Standard Deviation: " + str(standard3))

# '''
# townProb_Dictionary = {
#                     "(A, B)":0.1, 
#                     "(A, C)":0.9,
#                     "(B, D)":0.2,
#                     "(B, E)":0.8,
#                     "(C, E)":0.3,
#                     "(C, F)":0.7,
#                     "(D, G)":0.1,
#                     "(D, H)":0.9,
#                     "(E, H)":0.4,
#                     "(E, I)":0.6,
#                     "(F, I)":0.2,
#                     "(F, J)":0.8,
#                     "(G, K)":0.1,
#                     "(H, K)":0.3,
#                     "(H, L)":0.7,
#                     "(I, L)":0.5,
#                     "(I, M)":0.5,
#                     "(J, M)":1.0,
#                     "(K, N)":1.0,
#                     "(L, N)":0.4,
#                     "(L, O)":0.6,
#                     "(M, O)":1.0,
#                     "(N, P)":1.0,
#                     "(O, P)":1.0,
# }
# # print(townProb_Dictionary)

# minutesProb_Dictionary = {
#                     "(A, B)":5,
#                     "(A, C)":6,
#                     "(B, D)":4,
#                     "(B, E)":7,
#                     "(C, E)":4,
#                     "(C, F)":6,
#                     "(D, G)":4,
#                     "(D, H)":6,
#                     "(E, H)":6,
#                     "(E, I)":4,
#                     "(F, I)":3,
#                     "(F, J)":7,
#                     "(G, K)":4,
#                     "(H, K)":4,
#                     "(H, L)":8,
#                     "(I, L)":6,
#                     "(I, M)":4,
#                     "(J, M)":5,
#                     "(K, N)":4,
#                     "(L, N)":5,
#                     "(L, O)":6,
#                     "(M, O)":5,
#                     "(N, P)":5,
#                     "(O, P)":5,
# }
# '''
