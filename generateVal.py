import os
import sys
import json
from randomVal import generateRandOne

if __name__ == "__main__":
    print("ok")
    print(sys.argv)

#arguemnt 2 ouput file, 3 Poison 
if len(sys.argv) != 2:
    print("Not enough or too many arguements.")
    sys.exit(0)

print ("Enter the Posion mean")
val = input()
x = 0
try:
    x = int(val)
except ValueError:
    print("input is a string")
    sys.exit(0)

print ("Enter the std")
val2 = input()
a = ["a","b","c","d","e"]
periods = [5,10,15,20]
data = {"Interval": "100", "Containers": {} }

for n in a:
    data['Containers'][n] = {}
    data['Containers'][n]['Usages'] = []
    for w in periods:
         data['Containers'][n]['Usages'].append({"PeriodStartTime" : w, "ResourceDemand" : generateRandOne(x)})

with open("test files/" + sys.argv[1], "wt") as out:
    json.dump(data, out, indent = 4, sort_keys=True)
#print(generateRandtwo(6,3))
#print(generateRandtwo(6,3))
#print(generateRandtwo(6,3))
#print(generateRandOne(x))
#print(generateRandOne(x))
#print(generateRandOne(x))