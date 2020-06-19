import Power_Iteration as pi
import numpy as np
import networkx as nx

def power_iteration_application_test():
    A = np.array([[1.5, 0.5], [0.5, 1.5]])
    norm_indicator = True
    dom_eigenvector, dom_eigenvalue = pi.PowerMethod(A, norm_indicator, 0.01)
    print(dom_eigenvalue)
    print(dom_eigenvector)

def page_rank_application_test():
    G = nx.DiGraph()
    G.add_edges_from([(1,2),(2,3),(2,4), (3, 4),(3,5), (4, 5),(5,2),(5,4)])
    print(PageRank(G, 0.85))

def PageRank(G, weight):

    Aj = nx.adjacency_matrix(G)
    N = len(G.nodes)

    A = np.zeros(shape=(N,N))
    M = np.zeros(shape=(N,N))
    S = np.ones(shape = (N,N))
    for j, node in enumerate(G.nodes()):
        for i in range(N):
            A[i][j] = Aj[i][j]/G.out_degree(node)

    M =  A * (1-weight) -  S * weight


    print("under construction")
    return pi.PowerMethod(M,True, 0.01)



if __name__ == '__main__':
    power_iteration_application_test()

    page_rank_application_test()



