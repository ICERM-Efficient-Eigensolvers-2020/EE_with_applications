import numpy as np
import matplotlib.pyplot as plt

info_list = []
def InverseMethod(A, converge_range):
    
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

    while diff_list[idx] > converge_range:
        #solve the Aw = v^(k-1) for w=vec_new
        vec_new = np.linalg.solve(A, vec_list[idx]) 
        #normalize the newly found vec_new=w
        vec_new = vec_new / np.linalg.norm(vec_new)
        #add this to the vector list
        vec_list.append(vec_new)
        lambda_new = vec_new.dot(A.dot(vec_new))
        lambda_list.append(lambda_new)
        diff = np.abs(lambda_new - lambda_list[idx])
        diff_list.append(diff)
        idx = idx + 1
        
    print_log(idx, vec_list, lambda_list, diff_list)

    #plot lambda_list
    x = [i for i in range(idx+1)]
    if len(x) > 20:
        x = x[:21]
        diff_list = diff_list[:21]


    plt.plot(x, diff_list)
    plt.show()
    plt.savefig("II_difference_list_plot") 
    return vec_list[-1], lambda_list[-1]

def print_log(idx, vec_list, lambda_list, diff_list):
    print("Inverse Iteration:")
    print('Number of Iterations:', idx)
    cor_eig_vec = vec_list[idx]
    sm_eig_val = round(lambda_list[idx], 4)
    inv_eig_val = np.reciprocal(sm_eig_val)
    print('Inverse Smallest Eigenvalue:', inv_eig_val) #
    print('Smallest Eigenvalue:', sm_eig_val)
    print('Corresponding Eigenvector:', cor_eig_vec)
    print(diff_list[idx]) #don't really need this, just want to see it 


#Examples to run on
B = np.array([[1.5, 0.5], [0.5, 1.5]])
C = np.array([[2, 1], [2, 3]]) # eigenval of smallest magnitude of C is 1 
D = np.array([[2, 2, -1], [-5, 9, -3], [-4, 4, 1]]) # eigenvals of D are 3, 4, and 5 
E = np.array([[-4, 1, 1], [0, 3, 1], [-2, 0, 15]]) # eigenvals of E are ~ -3.9095, 3.0243 and 14.8852
F = np.array([[-6, 3], [4, 5]]) #eigenval of smallest magnitude of F is 6 with corresponding eigenvec [1, 4]
G = np.array([[0.8, 0.3], [0.2, 0.7]])
InverseMethod(D, 0.0001)