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
#Function: generate Unified independence sample with replacement
def UIS_WR(graph, count):
	return [random.choice(graph.keys()) for i in xrange(count)]

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
		
G = load_graph("p2p-Gnutella31.txt")
array=UIS_WR(G,10000)

edges =  nodestoEdgeList(G,array)

count = 0
traingle = []
for u,v in edges:
	temp = list(G[u] & G[v])
	for x in temp:
		if tuple(sorted((u,v,x))) in traingle:
			continue
		else:
			traingle.append(tuple(sorted((u,v,x))))


print len(traingle)
