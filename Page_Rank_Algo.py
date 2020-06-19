import Power_Iteration as pi
import numpy as np

def power_iteration_apply_test():
    A = np.array([[1.5, 0.5], [0.5, 1.5]])
    norm_indicator = True
    dom_eigenvector, dom_eigenvalue = pi.PowerMethod(A, norm_indicator, 0.01)
    print(dom_eigenvalue)
    print(dom_eigenvector)


def PageRank(diGraph):

    print("under construction")




if __name__ == '__main__':
    power_iteration_apply_test()



