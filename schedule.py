import os
import sys
import json
import random

def randomAssignment(conatiner, instances, avail):
    for contain in conatiner:
        count =0
        num =len(avail)
        if num != 1:
            num = random.randrange(1,len(avail))
        print(instances['Instances'])
        while True:
            if 'Instance' + str(num) in instances['Instances']:
                difference = avail['Instance' + str(num)]
                for n in instances['Instances']['Instance' + str(num)]['deployedCon']:
                    difference -= instances['Instances']['Instance' + str(num)]['deployedCon'][n]
                if conatiner[contain] <= difference:
                    instances['Instances']['Instance' + str(num)]['AvailRes'] = avail['Instance' + str(num)]
                    instances['Instances']['Instance' + str(num)]['deployedCon'][contain] = conatiner[contain]
                    break
            else:
                if conatiner[contain] <= avail['Instance' + str(num)]:
                    instances['Instances']['Instance' + str(num)] = {}
                    instances['Instances']['Instance' + str(num)]['deployedCon'] = {}
                    instances['Instances']['Instance' + str(num)]['AvailRes'] = avail['Instance' + str(num)]
                    instances['Instances']['Instance' + str(num)]['deployedCon'][contain] = conatiner[contain]
                    break
            num = num + 1 % len(avail)
            count +=1
            if count >=len(avail):
                print("could not assign resources")
                sys.exit(1)
    return instances

def evenAssignment(conatiner, instances, avail):
    lst = [0] * len(avail)
    for contain in conatiner:
        num = lst.index(min(lst)) + 1
        print(instances['Instances'])
        while True:
            if 'Instance' + str(num) in instances['Instances']:
                difference = avail['Instance' + str(num)]
                for n in instances['Instances']['Instance' + str(num)]['deployedCon']:
                    difference -= instances['Instances']['Instance' + str(num)]['deployedCon'][n]
                if conatiner[contain] <= difference:
                    instances['Instances']['Instance' + str(num)]['AvailRes'] = avail['Instance' + str(num)]
                    instances['Instances']['Instance' + str(num)]['deployedCon'][contain] = conatiner[contain]
                    lst[num-1] += 1
                    break
            else:
                if conatiner[contain] <= avail['Instance' + str(num)]:
                    instances['Instances']['Instance' + str(num)] = {}
                    instances['Instances']['Instance' + str(num)]['deployedCon'] = {}
                    instances['Instances']['Instance' + str(num)]['AvailRes'] = avail['Instance' + str(num)]
                    instances['Instances']['Instance' + str(num)]['deployedCon'][contain] = conatiner[contain]
                    lst[num-1] += 1
                    break
            num = lst.index(min(lst), num) + 1
            if num >=len(avail):
                print("could not assign resources")
                sys.exit(1)
    return instances

if __name__ == "__main__":
    print("ok")
    print(sys.argv)

RANGE_SET = 100
#arguement 1 arrangement file, arguemnt 2 supposed mean file, arguement 3 output file
if len(sys.argv) < 2:
    print("Not enough or too many arguements.")
    sys.exit(0)

stats = {"Instances" : {}}
print(stats)
contain = {}
avail = {}
print('Indicate how many Conatiners:')
x = input()
y = int(x)
for n in range(1, y+1):
    print('Assign Resources to container' + str(n))
    x = input()
    contain['Container' + str(n)] = int(x)
print(contain)

print('Indicate how many Instances:')
x = input()
t = int(x)
for n in range(1, t+1):
    print('Assign Resources to Instance' + str(n))
    x = input()
    avail['Instance' + str(n)] = int(x)
print(stats)
print("Random?")
while 1:
    x = input()
    if x == "y" or x =="yes":
        stats = randomAssignment(contain, stats, avail)
        break
    elif x == "n" or x =="no":
        stats = evenAssignment(contain, stats, avail)
        break

print(stats)    
with open("inputFiles/ContatinerDeployment/" + sys.argv[1], "wt") as out:
    json.dump(stats, out, indent = 4, sort_keys=True)


