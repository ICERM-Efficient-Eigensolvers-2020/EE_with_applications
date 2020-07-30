import sys, os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
from efficient_eigensolvers import PowerMethod, QR_unshifted, QR_shifted, RayleighQuotientIteration
from matricesGenerator import matrix_generator
import time
import math
import matplotlib.pyplot as plt
from scipy.linalg import hessenberg

if __name__ == '__main__':
    top_dim = 8
    dim_list = [2**i for i in range(2, top_dim)]
    func_list = [PowerMethod, QR_unshifted, QR_shifted, RayleighQuotientIteration]
    convergence_condition = 0.00001
    for func in func_list:
        time_list = []
        iteration_list = []
        for dim in dim_list:
            #average
            time_l = 0
            iteration = 0
            for _ in range(10):
                A, eigenvals = matrix_generator(dim)
                t_start = time.time()
                eigenvec, eigenval, iterations = func(A, convergence_condition)
                t_end = time.time()
                time_length = t_end - t_start
                time_l = time_l + time_length
                iteration = iteration + iterations
            time_l = time_l/10
            iteration = iteration/10
            time_list.append(time)
            iteration_list.append(iteration)

        plt.plot(dim_list, iteration_list, label= func.__name__)
        #plt.plot(dim_list, time_list ,label=func.__name__)
    plt.xlabel("Matrix Dimension")
    #plt.ylabel("Time")
    plt.ylabel("Iteration")
    plt.title("Performance Comparison")
    plt.legend()
    plt.savefig("performance_compare_iteration.png")
    plt.show()