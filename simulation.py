import os
import sys
import json
from randomVal import generateRandOne

if __name__ == "__main__":
    print("ok")
    print(sys.argv)

RANGE_SET = 100
#arguement 1 arrangement file, arguemnt 2 supposed mean file, arguement 3 output file
if len(sys.argv) != 4:
    print("Not enough or too many arguements.")
    sys.exit(0)

g = {'Containers': 
        {'C1': {'Mean': 40},
        'C2': {'Mean': 40},
        'C3': {'Mean': 60},
        }
    }
c = {'Instances':
        {
            'Instance1' :
                {
                    'AvailRes': 100,
                    'deployedCon' :
                        {
                            'C1': 50,
                            'C2': 50,
                        }
                },
            'Instance2' :
                {
                    'AvailRes': 120,
                    'deployedCon' :
                        {
                            'C3': 120
                        }
                }
        }
    }

with open("inputFiles/ContatinerDeployment/" + sys.argv[1]) as inputFile:
    c = json.load(inputFile)
with open("inputFiles/ContatinerStats/" + sys.argv[2]) as inputFile:
    g = json.load(inputFile)
#general structure
i = 0
resources = {}
stats = {}
compiled = {'Instances':{},'Average Usage': 0,'Total Unstatified Demand' :0}
totalPool = 0
availpool = 0
availRes = 0
totalrandomdemand = 0
unstatifieddemand = 0
unusedRes = 0
pool = 0
Utilization = 0

for x in c['Instances']:
    compiled['Instances'][x + ' Unstatified Demand'] = 0
for n in range(1,RANGE_SET + 1):
    i = 0
    stats[n] = {}
    totalPool = 0
    stats[n]['Total Unstatified Demand'] = 0
    stats[n]['Average Usage'] = 0
    #generate random resources
    for x in g['Containers']:
        #print(g['Containers'][x])
        resources[x] = generateRandOne(g['Containers'][x]['Mean'])
    stats[n]['Instances'] = {}
    for x in c['Instances']:
        i +=1
        availRes = c['Instances'][x]['AvailRes']
        availpool = c['Instances'][x]['AvailRes']
        totalPool = 0
        totalrandomdemand = 0
        unstatifieddemand = 0
        unusedRes = 0
        Utilization = 0
        for y in c['Instances'][x]['deployedCon']:
            pool = resources[y] - c['Instances'][x]['deployedCon'][y]
            totalrandomdemand += resources[y]
            unusedRes += max(-pool,0)
            availpool -= c['Instances'][x]['deployedCon'][y]
            if availpool < 0:
                availpool = 0
            if pool < 0:
                pool = 0
            totalPool += pool
        unstatifieddemand = max((totalPool - availpool)/totalrandomdemand,0)
        unusedRes += max(availpool - totalPool, 0)
        Utilization = 1 - (max(unusedRes,0)/availRes)
        """
        if x =="Instance2":
            print(c['Instances'][x]['deployedCon'][y])
            print(resources['C3'])
            print(unstatifieddemand)
            print(Utilization)
        """
        stats[n]['Instances'][x] = {'UnsatisfiedDemand' : unstatifieddemand, 'Utilization': Utilization}
        compiled['Instances'][x + ' Unstatified Demand'] += unstatifieddemand
        stats[n]['Total Unstatified Demand'] += unstatifieddemand
        stats[n]['Average Usage'] += Utilization

    stats[n]['Average Usage'] = stats[n]['Average Usage'] / len(c['Instances'])
    stats[n]['Total Unstatified Demand'] = stats[n]['Total Unstatified Demand'] / len(c['Instances'])
    compiled['Average Usage'] += stats[n]['Average Usage']
    compiled['Total Unstatified Demand'] += stats[n]['Total Unstatified Demand']
    #print(totalPool)
    #print(overflowed)
    
compiled['Average Usage'] = compiled['Average Usage']/RANGE_SET
compiled['Total Unstatified Demand'] = compiled['Total Unstatified Demand']/RANGE_SET
for x in c['Instances']:
    compiled['Instances'][x +' Unstatified Demand'] = compiled['Instances'][x + ' Unstatified Demand']/RANGE_SET
stats[0] = compiled
with open("output/" + sys.argv[3], "wt") as out:
    json.dump(stats, out, indent = 4, sort_keys=True)
