import numpy as np
import networkx as net
class cesna(object):
    
    derivMatF = []
    derivMatX = []
    derivMatX2 = []
    
    @staticmethod
    def calcDeriv(G,W,F):
        # the node attributes contain X for each node called X        
        #calculating the quantity Q
        Q = 1/(1+np.exp(-F*W.transpose()))
        exp = np.exp(-F*F.transpose())
        adjMat = net.to_numpy_matrix(G);
        X = net.get_node_attributes(G,'ID')
        # calculating the gradient of LG wrt Fu
        cesna.derivMatF = adjMat*F*exp/(1-exp)-(1-adjMat)*F
        cesna.derivMatX = (X-Q)*W
        cesna.derivMatX2 = F.transpose()*(X-Q)
        return
     
    @staticmethod 
    def update(G,W,F):
        alpha = 0.1
        cesna.calcDeriv(G,W,F)
        partial = cesna.derivMatF+cesna.derivMatX
        Fprime = np.max([0,F+alpha*partial])
        F = Fprime
        
        partial = cesna.derivMatX2
        W = W+ alpha*(partial-np.sign(W))
        
        return W,F