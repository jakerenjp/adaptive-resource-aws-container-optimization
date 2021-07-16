import os
import sys
import json
from randomVal import generateRandOne
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("ok")
    print(sys.argv)

RANGE_SET = 100
#arguement 1 arrangement file, arguemnt 2 supposed mean file, arguement 3 output file
if len(sys.argv) != 2:
    print("Not enough or too many arguements.")
    sys.exit(0)

with open("output/" + sys.argv[1]) as inputFile:
    c = json.load(inputFile)

x=[]
y={}
z = {}
z2 = []
for b in c["1"]["Instances"] :
    y[b] = []
    z[b] = []
for n in range(1,101):
    x.append(n-1)
    z2.append(c[str(n)]['Average Usage'])
    for b in c["1"]["Instances"] :
        y[b].append(c[str(n)]['Instances'][b]['UnsatisfiedDemand'])
        z[b].append(c[str(n)]['Instances'][b]['Utilization'])

plt.figure(1)
#plt.style.use('seaborn-whitegrid')
for b in c["1"]["Instances"] :
    plt.plot(x, y[b], label = b) 
# naming the x axis 
plt.xlabel('Simulation number') 
plt.xlim(0, 100)
# naming the y axis 
plt.ylabel('Unsatisfied Demand')
plt.ylim(0, 0.5)
# giving a title to my graph 
plt.title('Unsatisfied Demand of Instances') 
  
# show a legend on the plot 
plt.legend() 

plt.figure(2)
for b in c["1"]["Instances"] :
    plt.plot(x, z[b], label = b) 
# naming the x axis 
plt.xlabel('Simulation number') 
plt.xlim(0, 100)
# naming the y axis 
plt.ylabel('Utilization') 
plt.ylim(0, 1)
# giving a title to my graph 
plt.title('Utilization of Instance') 
  
# show a legend on the plot 
plt.legend() 

plt.figure(3)
plt.plot(x, z2, label = "Average Usage") 
# naming the x axis 
plt.xlabel('Simulation number') 
plt.xlim(0, 100)
# naming the y axis 
plt.ylabel('Utilization') 
plt.ylim(0, 1)
# giving a title to my graph 
plt.title('Utilization of All Instances') 
  
# show a legend on the plot 
plt.legend() 
# function to show the plot 
plt.show() 