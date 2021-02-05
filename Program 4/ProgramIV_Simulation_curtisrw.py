# Curt Wilson
# CS355 Program IV
# 3/18/2019

# ============================================================================================================

# Using Homework 8 as a guideline, write a program to simulate players A, B, and C in a season of 82 games. 
# Generate a string of shots for each player in each game, length 30, 20, and 10 shots. Count the number of
# shots each makes.

# Accumulate and make histograms of the following statistics:

# Total made shots for all three players per game.
# Total made shots for player A per game.
# Total made shots for player B per game.
# Total made shots for player C per game.
# Which of these histograms resemble a Normal distribution?

# ============================================================================================================
from random import *

#  

playerA = []   
playerB = []    
playerC = []     

resultsA = []
resultsB = []
resultsC = []

file1 = open("results1.txt" , 'w+')
file2 = open("results2.txt" , 'w+')
file3 = open("results3.txt" , 'w+')
def basketballSim(games):
    for i in range(games):
        for _ in range(30):
            rand = randint(0, 10) / 10
            # create a bias of 70% chance
            if rand <= 0.7:
                playerA.append(1)
            else:
                playerA.append(0)

        for _ in range(20):
            rand = randint(0, 10) / 10
            # create a bias of 60% chance
            if rand <= 0.6:
                playerB.append(1)
            else:
                playerB.append(0)

        for _ in range(10):
            rand = randint(0, 10) / 10
            # create a bias of 50% chance
            if rand <= 0.5:
                playerC.append(1)
            else:
                playerC.append(0)
        A_shots=sum(playerA)
        B_shots=sum(playerB)
        C_shots=sum(playerC)
        A_average = A_shots/len(playerA)
        B_average = B_shots/len(playerB)
        C_average = C_shots/len(playerC)

        resultsA.append(A_average)
        resultsB.append(B_average)
        resultsC.append(C_average) 
        
    for i in range(games):
        file1.write(str(resultsA[i]) + "\t\n")
        file2.write(str(resultsB[i])+ "\t\n")
        file3.write(str(resultsC[i]) + "\t\n")   

    print("Player A's Averages: \n")
    print(resultsA)
    print("\nPlayer B's Averages: \n")
    print(resultsB)
    print("\nPlayer C's Averages: \n")
    print(resultsC)

    
    file1.close()
    file2.close()
    file3.close()
    # plt.grid(True)
    # num_bins = 10
    # n, bins, patches = plt.hist(resultsA, num_bins, facecolor='blue', alpha=0.5)
    # # plt.hist(resultsA, weights=True, bins='auto')
    # plt.title("Player A Shot Statistics")
    # plt.show()

    # print('Histogram')
    # print('A stats {0}/{1} - {2}'.format(A_shots,len(playerA),'*'*A_shots))
    # print('B stats {0}/{1} - {2}'.format(B_shots,len(playerB),'*'*B_shots))
    # print('C stats {0:>2}/{1:>2} - {2}'.format(C_shots,len(playerC),'*'*C_shots))
basketballSim(82)

