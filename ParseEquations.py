#!/usr/bin/python
import json, statistics, math, scipy
from scipy import stats

def findContainer(containerName, containers):

	if containerName not in containers.keys():
		return

	usages = containers.get(containerName).get("Usages")
	resourceList = []
	for usage in usages:
		resourceList.append(int(usage.get("ResourceDemand")))

	return resourceList

def findInstanceAvaR(instanceName, instances):
	if instanceName not in instances.keys():
		return

	instanceValues = instances.get(instanceName)
	avaR = int(instanceValues.get("AvaR"))
	return avaR

def findInstanceCost(instanceName, instances):
	if instanceName not in instances.keys():
		return

	instanceValues = instances.get(instanceName)
	cost = int(instanceValues.get("Cost"))
	return cost


def containerMean(resourceList):
	return statistics.mean(resourceList)

def containerStdDev(resourceList):
	return statistics.stdev(resourceList)

def findContainersSubset(containerNameList, containers):

	subsetList = []
	for container in containerNameList:
		subsetList.extend(findContainer(container, containers))

	return subsetList

def normalUpperBound(resourceList, confidence):
	eventTotal = len(resourceList)
	mean = containerMean(resourceList)
	upperBound = 0
	if confidence == 95:
		upperBound = mean + 1.96 * math.sqrt(mean/eventTotal)
	elif confidence == 99:
		upperBound = mean + 2.60 * math.sqrt(mean/eventTotal)

	return upperBound

def poissonUpperBound(resourceList, confidence):
	eventTotal = len(resourceList)
	mean = containerMean(resourceList)
	total = mean * eventTotal
	confInv = 100 - confidence
	totalUpperBound = scipy.stats.chi2.ppf((100 - confInv/2) * 0.01, 2*(total+1))/2
	upperBound = totalUpperBound/eventTotal

	return upperBound

class Container:
	def __init__(self, name, usage):
		self.Name = name
		self.MeanUsage = usage

class Instance:
	def __init__(self, name, availableResource, cost):
		self.Name = name
		self.AvailableResource = availableResource
		self.Cost = cost
	

data = {}

with open('testdata.json') as f:
	data = json.load(f)

containers = data.get('Containers')
instances = data.get('Instances')
container1Resources = findContainer("Container1", containers)
container1Mean = containerMean(container1Resources)
container2Resources = findContainer("Container2", containers)
container2Mean = containerMean(container2Resources)
container3Resources = findContainer("Container3", containers)
container3Mean = containerMean(container3Resources)

instance1AR = findInstanceAvaR("Instance1", instances)
instance2AR = findInstanceAvaR("Instance2", instances)
instance3AR = findInstanceAvaR("Instance3", instances)
instance1Cost = findInstanceCost("Instance1", instances)
instance2Cost = findInstanceCost("Instance2", instances)
instance3Cost = findInstanceCost("Instance3", instances)

Containers = [Container('Container1', container1Mean),Container('Container2', container2Mean),Container('Container3', container3Mean)]
Instances = [Instance('Instance1', instance1AR, instance1Cost),Instance('Instance2', instance2AR, instance2Cost),Instance('Instance3', instance3AR, instance3Cost)]

"""data = {}

with open('testdata.json') as f:
	data = json.load(f)

containers = data.get('Containers')

testContainerList = findContainer("ContainerName", containers)
testContainerList2 = findContainer("ContainerName2", containers)

print(normalUpperBound(testContainerList, 95))
print(poissonUpperBound(testContainerList, 95))"""

'''
{
“Interval” : “100”,
“Containers” : 
	{“ContainerName” : 
		{ “Usages" : 
			[
				{“PeriodStartTime” : “0”, “ResourceDemand" : “92”},
				{“PeriodStartTime” : “5”, “ResourceDemand” : “82”},
				{“PeriodStartTime”: “10”, “ResourceDemand” : “92”},
				…….
				{“PeriodStartTime”: “95”, “ResourceDemand” : “92”},
			]
		},
	“ContainerName2” : {...},
	“ContainerName3” : {...},
	….
	“ContainerNameN”: {///}
	}
“Instances” : 
	{“InstanceName” : 
		{ "AvaR" : "100"
		  "Cost" : "100"
		},
	}
}
'''