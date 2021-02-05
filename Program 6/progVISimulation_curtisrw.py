# Curt Wilson
# CS355_ProgramVI
# 4/15/2019


# Write a program to simulate the journey from A to D, for each airline, using the
# data above. Generate a large number of trials for each airline (maybe 10,000 would be enough),
# compute the arrival time for the rest flight at B or E, and decide which second 
# flight you will be able to take. Compute the arrival time at C or F, decide which third 
# flight you will be able to take, and compute the average arrival time at D for both options.
# If you arrive at B or E too late to take the second flight, count the trip as having been
# stranded, and the same for arriving at C or F too late for the third connecting flight.
# Compare arrival times at city D for the two options. For each option, Airline One and
# Airline Two, display:
# 1. average arrival time
# 2. probability of arriving by 30 minutes after scheduled time (21:00 for Airline
# One/20:00 for Airline Two)
# 3. probability of being stranded
# You may assume departing flights are at gates next to arrivals, so that if a flight
# arrives within one minute of departure for the next time, the second 
# flight may be used. Assume a minimum flight time of mu - 3(sigma) and a maximum time of mu + 3(sigma). If 
# flight times fall out side these limits, change them to the max or min.

import random
import numpy as np
from math import *

# f = open("ProgramVI_Results_curtisrw.txt","a+")

timeArray = []
missedTime = []
directTime = []
lateArray = []
average = 0
timeCalc = 8

def firstAirline():
    s3 = random.uniform(0,100)
    s4 = random.uniform(0,100)
    mu = 4   # mean, or avg
    standardDev = .4   # standard deviation
    timeCalc = 8   # flight leaves at 8 AM

    if (mu == 4 and standardDev == .4):
        q = random.uniform(3,5)
        result = 100*(0.997356*exp(-3.125*(q-4)**2))
        if (result <= s3):
            timeCalc = timeCalc + q
            timeArray.append(timeCalc)
            directTime.append(1)

        else:
            missedTime.append(1)
            lateArray.append(1)
         

    if (mu == 4 and standardDev == .4):
        q = random.uniform(3,5)
        result = 100*(0.664904*exp(-1.38889*(q-4)**2))
        if (result <= s4):
            timeCalc = timeCalc + q
            timeArray.append(timeCalc)
            mu = 3.5
            directTime.append(1)
             

        else:
            missedTime.append(1)
            lateArray.append(1)
             

    if (mu == 3.5 and standardDev == .4):
        q = random.uniform(2.5,4.5)
        result = 100*(0.664904*exp(-1.38889*(q-3.5)**2))
        timeCalc = timeCalc + q
        timeArray.append(timeCalc)
        directTime.append(1)
         

def secondAirline():
    s1 = random.uniform(0,100)
    s2 = random.uniform(0,100)
    mu = 3.5   # mean, or avg
    standardDev = .6   # standard deviation
    timeCalc = 8   # flight leaves at 8 AM

    if (mu == 3.5 and standardDev == .6):
        q = random.uniform(2,5)
        result = 100*(0.664904*exp(-1.38889*(q-3.5)**2))
        if (result <= s1):
            timeCalc = timeCalc + q
            timeArray.append(timeCalc)
            directTime.append(1)
            mu = 4
             

        else:
            missedTime.append(1)
            lateArray.append(1)
             

    if (mu == 4 and standardDev == .6):
        q = random.uniform(2.5,5.5)
        result = 100*(0.664904*exp(-1.38889*(q-4)**2))
        if (result <= s2):
            timeCalc = timeCalc + q
            timeArray.append(timeCalc)
            directTime.append(1)
            mu = 3.5
             
        else:
            missedTime.append(1)
            lateArray.append(1)
             

    if (mu == 3.5 and standardDev == .6):  # if conditions are true, you have arrived
        q = random.uniform(2,5)
        result = 100*(0.664904*exp(-1.38889*(q-3.5)**2))
        timeCalc = timeCalc + q
        timeArray.append(timeCalc)
        directTime.append(1)
         

def simulate():
    for sim in range(10000):
        firstAirline()
    print("**************** AIRLINE 1 SIMULATION ****************")
    hours = sum(timeArray)/len(timeArray)
    minutes = 60*(hours%1)
    print("Average time of arrival:" ,"%d:%02d" % (hours, minutes))
    print("Chances of you arriving 30 mins late: ", 100*(sum(lateArray)/sum(directTime)), "%")
    print("Chances that you could be stranded: ", 100 *(sum(missedTime)/10000), "%")
    

    # f.write("**************** AIRLINE 1 SIMULATION ****************")
    # f.write("Chances that you could be stranded: ", 100 *(sum(missedTime)/10000), "%")
    # f.write("Chances of you arriving 30 mins late: ", 100*(sum(lateArray)/sum(directTime)), "%")
    # f.write("Average time of arrival:" ,"%d:%02d" % (hours, minutes))


    for sim in range(10000):
        secondAirline()

    print("\n**************** AIRLINE 2 SIMULATION ****************")
    hours = sum(timeArray)/len(timeArray)
    minutes = 60*(hours%1)
    print("Average time of arrival:" ,"%d:%02d" % (hours, minutes))
    print("Chances of you arriving 30 mins late: ", 100*(sum(lateArray)/sum(directTime)), "%")
    print("Chances that you could be stranded: ", (sum(missedTime)/10000), "%")
    

    # f.write("\n**************** AIRLINE 2 SIMULATION ****************")
    # f.write("Chances that you could be stranded: ", (sum(missedTime)/10000), "%")
    # f.write("Chances of you arriving 30 mins late: ", 100*(sum(lateArray)/sum(directTime)), "%")
    # f.write("Average time of arrival:" ,"%d:%02d" % (hours, minutes))

simulate()

#################################################################################################
#################################################################################################

