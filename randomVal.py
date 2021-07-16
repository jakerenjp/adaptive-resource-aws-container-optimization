import math
import random

#credit here https://www.johndcook.com/blog/2010/06/14/generating-poisson-random-values/
def generateRandOne(mean):
    L = math.exp(-mean)
    k = 0
    p = 1.0
    while p > L:
        k = k+1
        p = p * random.random()
    return k

def generateRandtwo(mean, std):
    k = random.randint(0,100)
    s = mean + (math.pow(mean, k) * math.exp(-mean) * std / math.factorial(k))
    return s