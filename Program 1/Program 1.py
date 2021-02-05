# Curt Wilson
# CS355_Program1
# Started 1/22/2019

'''
Simulate the following population system:
There are 100 mitochondrial DNA (mDNA) groups, each with 100 members, 50 male and 50 female.
Write a program to simulate population growth, tracking the sizes of mDNA groups. To simplify, assume the members of the 
population marry at random and that they have children in distinct generations. For each generation, marry males and females 
picked at random, and assign each family 0, 1, 2, or 3 children, each randomly male or female, P(male) = P(female) = .5, and 
for family size, assume P(0) = P(1) = P(2) = P(3) = .25 children.

Starting with a population of 10,000, how does the population increase or decrease? 
How does sizes of mDNA groups change? Do any disappear, and if so, how does the number of mDNA groups change with time.
Change population size probabilities to 
P(0) = 1/12, P(1) = 3/12, P = 7/12, P(3) = 1/12 and answer the same questions.
Change population size probabilities to 
P(0) = 1/11, P(1) = 2/11, P = 6/11, P(3) = 2/11 and answer the same questions.
'''

import random

class DNA(self, Male, Female):
    self.Male = male
    self.Female = female

class Generations(self, marry, children):
    mDNA = 100
    maleCount = 0
    femaleCount = 0
    for x in range(50):
        marry = random.choice(Male, Female)
        for marry in range(50):
            if r < 1/12:
                print("0")
                return 0
            elif r < 3/12:
                print("1")
                return 1
            elif r < 7/12:
                print("2")
                return 2
            elif r < 11/12:
                print("3")
                return 3
def simulate()
    for simulate in range(simulate):
    
simulate(1/12)
simulate(2/12)
