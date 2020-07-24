import sys, os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
eigensovers_folder = THIS_FOLDER[:-25] + "efficientEigensolvers/"
sys.path.append(eigensovers_folder)
import matricesGenerator
import time

import Page_Rank_Utils as pru
from Power_Iteration import PowerMethod
from QR_Algorithm import qr_Algorithm_HH, qr_Algorithm_GS, shiftedQR_Algorithm
from Inverse_Iteration import InverseMethod
from Inverse_Iteration_w_shift import InverseShift
import matplotlib.pyplot as plt


if __name__ == '__main__':
    dim_list = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 9192]
    func_list = [PowerMethod, qr_Algorithm_HH, qr_Algorithm_GS, shiftedQR_Algorithm, InverseMethod, InverseShift]
    func_list = [PowerMethod]
    converge_range = 0.00001
    for dim in dim_list:
        #random A
        A = matricesGenerator(dim)
        t_start = time.time()
        for func in func_list:
            eigenvec, eigenval = func(A, converge_range=converge_range)
        t_end = time.time()
        time_length = t_end - t_start
