import networkx as netg
import numpy as np
from CESNA import cesna as cs

def bin_search(arr,elem,start,end):
    mid = (start+end)/2;
    if start == end:
        return -1
        
    if arr[mid]==elem:
        return mid
    elif arr[mid] > elem:
        return bin_search(arr,elem,start,mid)
    else:
        return bin_search(arr,elem,mid,end)



data = open("/home/abhishek/Personal/machine learning/project/Datasets/email-EU/data.txt", "r")
lines = data.read().split('\n')
lines.pop()

data.close()

srcID = []
destID = []
timestamp = []

G = netg.Graph()
nodes = {}

for i in range(len(lines)):
    lines[i]=lines[i].split(" ")
    for j in range(len(lines[i])):
        lines[i][j]=int(lines[i][j])
    srcID.append(lines[i][0])
    destID.append(lines[i][1])
    timestamp.append(lines[i][2])

srcID.extend(destID)
nodes = list(set(srcID))

for i in range(len(nodes)):
    G.add_node(i,{'ID':nodes[i]})
    

for i in range(len(lines)):
    row = bin_search(nodes,srcID[i],0,len(nodes))
    col = bin_search(nodes,destID[i],0,len(nodes))
    G.add_edge(row,col)

    
numCommunity = 30
numNodes = len(G.nodes())
numAttrib = len(G.node[1])

W = np.random.rand(numAttrib,numCommunity)
W = np.asmatrix(W)
F = (np.random.rand(numNodes,numCommunity) > 0.5).astype(int)
F = np.asmatrix(F)

cnt = 0;

while cnt < 20:
    W,F = cs.update(G,W,F)
    print cnt
    cnt += 1
    
    
    
