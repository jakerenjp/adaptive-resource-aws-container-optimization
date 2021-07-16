from pulp import *
import ParseEquations
import json

Alpha = 0.20 #constant
Beta = 0.95 #constant

#LP variable definitions
NumberOfContainers = len(ParseEquations.Containers)
NumberOfIInstances = len(ParseEquations.Instances)
XMat = LpVariable.dicts("Matrix", ((i, j) for i in range(NumberOfContainers) for j in range(NumberOfIInstances)), 0, 1, cat='Integer')
InstanceUsage_var = LpVariable.dicts("InstanceUsage", (j for j in range(NumberOfIInstances)), 0 , 1, cat='Integer')

prob = LpProblem("CloudOpt", LpMinimize)
prob += lpSum([ParseEquations.Instances[j].Cost * InstanceUsage_var[j] for j in range(NumberOfIInstances)]), "Total Cost "


for j in range(NumberOfIInstances): 
  for i in range(NumberOfContainers): 
    prob += InstanceUsage_var[j] >= XMat[(i,j)]

for i in range(NumberOfContainers): 
  prob += lpSum([XMat[(i, j)] for j in range(NumberOfIInstances)]) == 1

for j in range(NumberOfIInstances): 
  prob += lpSum([XMat[(i, j)]*ParseEquations.Containers[i].MeanUsage*Alpha for i in range(NumberOfContainers)]) + lpSum([XMat[(i, j)]*ParseEquations.Containers[i].MeanUsage*Beta for i in range(NumberOfContainers)]) <= ParseEquations.Instances[j].AvailableResource

prob.writeLP('eqation.lg')
prob.solve()
print("Status:", LpStatus[prob.status])
print("All variables:")
for v in prob.variables():
    print(v.name, "=", v.varValue)

data = {}
data['Instances'] = {}
j = 0
for instance in ParseEquations.Instances:
    if(InstanceUsage_var[j].varValue == 0):
        j += 1
        continue
    data['Instances'][instance.Name] = {
        'AvailRes' : instance.AvailableResource,
        'deployedCon': {}
    }
    for i in range(NumberOfContainers):
        if XMat[(i,j)].varValue == 1:
            data['Instances'][instance.Name]['deployedCon'][ParseEquations.Containers[i].Name] = ParseEquations.Containers[i].MeanUsage * Alpha
    j += 1


with open("Schedule.json", "wt") as out:
    json.dump(data, out, indent = 4)

containersData = {}
containersData["Containers"] = {}
for c in ParseEquations.Containers:
    containersData["Containers"][c.Name] = {}
    containersData["Containers"][c.Name]['Mean'] = c.MeanUsage

with open("Containers.json", "wt") as containerJson:
    json.dump(containersData, containerJson, indent = 4)




#prob += lpSum([XMat[(i,'Instance1')] for i in ContainerSets]) == 1  