import numpy as np
from tabulate import tabulate

info_list = []
def PowerMethod(A, norm_indicator, converge_range):

    r, c = A.shape

    if r != c:
        raise Exception("not a square matrix")

    #initialize eigenvectors
    v_list = []
    lambda_list = []
    diff_list = []

    idx = 0
    v_init = np.zeros(r)
    v_init[-1] = 1
    v_list.append(v_init)

    #initialize eigenvalues
    lambda_init = v_init.dot(A.dot(v_init))
    lambda_list.append(lambda_init)
    
    diff_init = float("inf")
    diff_list.append(diff_init)

    while diff_list[idx] > converge_range:
        #new vector
        v_new = A.dot(v_list[idx])
        v_list.append(v_new)
        if norm_indicator:
            v_new = v_new / np.linalg.norm(v_new) 
        lambda_new = v_new.dot(A.dot(v_new))    
        lambda_list.append(lambda_new)
        diff = np.abs(lambda_new - lambda_list[idx])
        diff_list.append(diff)
        idx = idx + 1

    print_log(idx, v_list, lambda_list, diff_list)
    return v_list[-1], lambda_list[-1]

def print_log(idx, v_list, lambda_list, diff_list):
    info_list = [[i,v_list[i],lambda_list[i],diff_list[i]] for i in range(idx)]
    print(tabulate(info_list, headers=["iteration","eigenvector", "eigenvalue","err"]))


