from scipy.stats import ortho_group
import random
import numpy as np

def lambda_generator(dim):
    randomlist = [random.random() for i in range(0, dim)]
    return randomlist


def matrix_generator(dim):
    M = ortho_group.rvs(dim=dim)
    lambdas = lambda_generator(dim)
    D = np.zeros((dim, dim), float)
    np.fill_diagonal(D, lambdas)
    A = np.matmul(M, D)
    A = np.matmul(A, np.linalg.inv(M))

    return A, lambdas
