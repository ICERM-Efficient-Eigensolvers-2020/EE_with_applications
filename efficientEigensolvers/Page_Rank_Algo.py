import Power_Iteration as pi
import numpy as np
import networkx as nx
import scipy

from matplotlib import pyplot as plt

def power_iteration_application_test():
    A = np.array([[1.5, 0.5], [0.5, 1.5]])
    print(A)
    norm_indicator = False
    dom_eigenvector, dom_eigenvalue = pi.PowerMethod(A, norm_indicator, 0.0001)
    print(dom_eigenvalue)
    print(dom_eigenvector)

    norm_indicator = True
    dom_eigenvector, dom_eigenvalue = pi.PowerMethod(A, norm_indicator, 0.0001)
    print(dom_eigenvalue)
    print(dom_eigenvector)



def page_rank_application_test():
    G = nx.DiGraph()
    G.add_edges_from([(1,2),(1,3),(1,4),(2,3),(2,4), (3, 1),(4,1), (4, 3)])
    nx.draw(G, with_labels=True)
    plt.savefig("page_rank_application_sample.png")
    plt.show()
    print("Limiting Distribution: ")
    print(PageRank(G, 0.15))


def PageRank(G, weight):

    Aj = nx.to_numpy_matrix(G).A
    N = len(G.nodes)

    A = np.zeros(shape=(N,N))
    S = np.ones(shape = (N,N))
    S = np.multiply(S, 1/N)

    for j, node in enumerate(G.nodes()):
        out_deg = G.out_degree(node)
        for i in range(N):

            A[i][j] = Aj[i][j]/out_deg

    Aw = np.multiply(A, 1 - weight)
    Sw = np.multiply(S, weight)
    M = Aw + Sw

    return pi.PowerMethod(M,True, 0.01)[0]



if __name__ == '__main__':
    print("###Power Iteration Test###")
    power_iteration_application_test()

    #print("###Page Rank Test###")
    #page_rank_application_test()



