from scipy.stats import ortho_group
import random
import numpy as np

def lambda_generator(dim):
    randomlist = []
    for i in range(0, dim):
        n = random.random()
    randomlist.append(n)
    return randomlist


def matrix_generator(dim):
    M = ortho_group.rvs(dim=dim)
    lambdas = lambda_generator(dim)
    D = np.zeros((dim, dim), float)
    np.fill_diagonal(D, lambdas)
    A = np.zeros(shape=(dim,dim), dtype=float)
    for j in range(dim):
        A = A + M[:, j].dot(M[:,j].T) * lambdas[j]

    return A
