import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt
import Page_Rank_Utils as pru


def detectedConverged(y,x,epsilon):
    C = set()
    N = set()
    for i in range(len(y)):
        if abs(y[i] - x[i])/abs(x[i]) < epsilon:
            C.add(i)
        else:
            N.add(i)
    return N, C


def filter(A_prime, x_prime, N, C):
    n = N.shape[0]
    for i in range(n):
        if i in C:
            x_prime[i] = 0
            for j in range(n):
                A_prime[i][j] = 0
    return A_prime, x_prime


def Filter_APR(G, weight, period):

    P = pru.stochastic_transition_matrix(G, weight, True)
    n = P.shape[0]

    # initialize eigenvectors
    v_list = []

    idx = 0
    v_init = np.zeros(n)
    v_init[-1] = 1
    v_list.append(v_init)
    converged = True
    while not converged:
        return






