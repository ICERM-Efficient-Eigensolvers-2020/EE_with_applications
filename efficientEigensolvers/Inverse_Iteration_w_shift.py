import numpy as np
import tabulate
import matplotlib.pyplot as plt
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

info_list = []
def InverseShift(A, mu=1.1, converge_range=0.0001, file_path="."):
    
    r, c = A.shape

    if r != c:
        raise Exception("not a square matrix")

    #initialize eigenvectors
    vec_list = []
    lambda_list = []
    diff_list = []

    idx = 0
    vec_init = np.zeros(r)
    vec_init[-1] = 1
    vec_list.append(vec_init)

    #initialize eigenvalues
    lambda_init = vec_init.dot(A.dot(vec_init))
    lambda_list.append(lambda_init)
    
    diff_init = float("inf")
    diff_list.append(diff_init)

    I = np.identity(r)

    while diff_list[idx] > converge_range:
        mat = A - (mu*I)
        #solve the (A-(mu)I)w = v^(k-1) for w=vec_new
        vec_new = np.linalg.solve(mat, vec_list[idx]) 
        #normalize the newly found vec_new=w
        vec_new = vec_new / np.linalg.norm(vec_new)
        #add this to the vector list
        vec_list.append(vec_new)
        lambda_new = vec_new.dot(A.dot(vec_new))
        lambda_list.append(lambda_new)
        diff = np.abs(lambda_new - lambda_list[idx])
        diff_list.append(diff)
        idx = idx + 1
        
    print_log(idx, vec_list, lambda_list, diff_list, file_path)

    #plot lambda_list
    x = [i for i in range(idx+1)]
    if len(x) > 20:
        x = x[:21]
        diff_list = diff_list[:21]


    plt.plot(x, diff_list)
    plt.title("Inverse Iteration with Shift Lambda Difference")
    plt.xlabel('iterations')
    plt.ylabel('lambda difference')
    plt.savefig(file_path+ "/IwS_difference_list_plot")
    plt.show()

    return vec_list[-1], lambda_list[-1]


def print_log(idx, vec_list, lambda_list, diff_list, file_path):
    info_list = [[i, vec_list[i], lambda_list[i], diff_list[i]] for i in range(idx)]
    print(file_path)
    with open(file_path+'/Inverse_Shift_performance.txt', 'w') as outputfile:
        outputfile.write(tabulate(info_list, headers=["iteration","eigenvector", "eigenvalue","lambda_diff"]))
