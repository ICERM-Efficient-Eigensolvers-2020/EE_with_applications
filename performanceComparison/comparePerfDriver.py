import sys, os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
from efficient_eigensolvers import PowerMethod, QR_unshifted, QR_shifted, QR_wilkinson_shift, RayleighQuotientIteration
from matricesGenerator import matrix_generator
import time
import math
import matplotlib.pyplot as plt
from scipy.linalg import hessenberg
import csv

import seaborn as sns
"""
sns.set(font='Franklin Gothic Book',
        rc={
 'axes.axisbelow': False,
 'axes.edgecolor': 'lightgrey',
 'axes.grid': False,
 'axes.labelcolor': 'dimgrey',
 'axes.spines.right': False,
 'axes.spines.top': False,
 'figure.facecolor': 'white',
 'lines.solid_capstyle': 'round',
 'patch.edgecolor': 'w',
 'patch.force_edgecolor': True,
 'text.color': 'dimgrey',
 'xtick.bottom': False,
 'xtick.color': 'dimgrey',
 'xtick.direction': 'out',
 'xtick.top': False,
 'ytick.colo': 'dimgrey',
 'ytick.direction': 'out',
 'ytick.left': False,
 'ytick.right': False})
"""
sns.set_context("notebook", rc={"font.size":16,
                                "axes.titlesize":20,
                                "axes.labelsize":18})

if __name__ == '__main__':
    with open('performance_comparison.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        top_dim = 50
        dim_list = [5+10*i for i in range(top_dim)]
        func_list = [QR_unshifted, QR_shifted, QR_wilkinson_shift]
        convergence_condition = 0.0001
        for func in func_list:
            iteration_w_hessen_list = []
            iteration_wo_hessen_list = []
            for dim in dim_list:
                iteration_wo_hessen = 0
                iteration_w_hessen = 0

                for _ in range(100):
                    #generate the random matrix
                    A, eigenvals = matrix_generator(dim)
                    eigenvec, eigenval, iterations = func(A, convergence_condition)
                    iteration_wo_hessen = iterations/100 + iteration_wo_hessen

                    #with_hessenberge:
                    H,Q = hessenberg(A, calc_q=True)
                    eigenvec, eigenval, iterations = func(H, convergence_condition)
                    iteration_w_hessen = iterations/100 + iteration_w_hessen

                iteration_wo_hessen_list.append(iteration_wo_hessen)
                iteration_w_hessen_list.append(iteration_w_hessen)

            csvwriter.writerow([{func.__name__}])
            csvwriter.writerow(iteration_wo_hessen_list)
            csvwriter.writerow(iteration_w_hessen_list)
            plt.plot(dim_list, iteration_wo_hessen_list, label=f'{func.__name__} W/O Hessenberg')
            plt.plot(dim_list, iteration_w_hessen_list, label=f'{func.__name__} W Hessenberg')



        plt.xlabel("Matrix Dimension")
        plt.ylabel("Iteration")
        plt.title("Performance Comparison")
        sns.despine(left=True, bottom=True)
        plt.legend(frameon=False)
        plt.savefig("performance_compare_iteration.png")
        plt.show()