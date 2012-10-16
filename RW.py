import random
from random import choice

#Function: Load graph from a file
def load_graph(fname):
    fr = open(fname, 'r')
    G = {}   
    for line in fr:
        if not line.startswith('#'):
		a,b = map(int, line.split())    
            	if a not in G:  G[a] = set()
            	if b not in G:  G[b] = set()        
            	G[a].add(b)
            	G[b].add(a)    
    fr.close()    
    return G
#Function: generate random walk
def random_walk(graph, seed, count,safety_margin):
	i=0
	array=[]
	element = choice(list(graph[seed]))
	array.append(element)
	i+=1
	while i<count*safety_margin:
		element = choice(list(graph[array[-1]]))
		array.append(element)
		i+=1
	return array[::safety_margin]

#Function: nodes to edgeList
def nodestoEdgeList(graph, array):
	edgeList=[]	
	for x in array:
		for j in list(graph[x]):
			if tuple(sorted((x,j))) in edgeList:
				continue
			else:
				edgeList.append(tuple(sorted((x,j))))
	return edgeList
		
safety_margin=10
G = load_graph("p2p-Gnutella31.txt")
array=random_walk(G,42,10000,safety_margin)
#G={1:set([3,2]),2:set([1,3,4]),3:set([1,2,4]),4:set([2,3])}
edges =  nodestoEdgeList(G,array)
#edges = [(1,2),(1,3),(2,3),(2,4),(3,4)]

traingle = []
for u,v in edges:
	temp = list(G[u] & G[v])
	for x in temp:
		if tuple(sorted((u,v,x))) in traingle:
			continue
		else:
			traingle.append(tuple(sorted((u,v,x))))


print len(traingle)
