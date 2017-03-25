import numpy as np
import networkx as net
class cesna(object):
    
    derivMatF = []
    derivMatX = []
    derivMatX2 = []
    
    def calcDeriv(G,W,F):
        # the node attributes contain X for each node called X        
        #calculating the quantity Q
        Q = 1/(1+np.exp(-W*F.transpose()))
        exp = np.exp(-F*F.transpose())
        adjMat = net.to_numpy_matrix(G);
        X = net.get_node_attributes(G,'X')
        # calculating the gradient of LG wrt Fu
        derivMatF = adjMat*F*exp/(1-exp)-(np.identity(len(F))-adjMat)*F
        derivMatX = (X-Q)*W
        derivMatX2 = (X-Q)*F.transpose()        
        return
        
    def update(G,W,F):
        alpha = 0.1
        obj = cesna()
        
        
        obj.calcDeriv(G,W,F)
        partial = obj.derivMatF+obj.derivMatX
        Fprime = np.max([0,F+alpha*partial])
        F = Fprime
        
        partial = derivMatX2
        W = W+ alpha*(partial-np.sign(W))
        