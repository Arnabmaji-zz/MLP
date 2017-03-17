import networkx as netg
import matplotlib.pyplot as plt
import community

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



data = open("/home/arnab/MLP/data", "r")
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
        #print lines[i][j],"..............................................."
        lines[i][j]=int(lines[i][j])
    srcID.append(lines[i][0])
    destID.append(lines[i][1])
    timestamp.append(lines[i][2])

#Constructing the adjacency matrix
srcID.extend(destID)
nodes = list(set(srcID))
nodes.sort()
# constructing the graph
G.add_nodes_from(nodes)
for i in range(len(lines)):
    row = bin_search(nodes,srcID[i],0,len(nodes))
    col = bin_search(nodes,destID[i],0,len(nodes))
    G.add_edge(row,col)

    
partition = community.best_partition(G);
size = float(len(set(partition.values())))
pos = netg.spring_layout(G)
count = 0.
for com in set(partition.values()) :
    count = count + 1.
    list_nodes = [nodes2 for nodes2 in partition.keys()
                                if partition[nodes2] == com]
    netg.draw_networkx_nodes(G, pos, list_nodes, node_size = 20,
                                node_color = str(count / size))


netg.draw_networkx_edges(G,pos, alpha=0.5)