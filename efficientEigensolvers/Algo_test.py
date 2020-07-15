from Power_Iteration import PowerMethod
from QR_Algorithm import qr_Algorithm_HH, qr_Algorithm_GS, shiftedQR_Algorithm
from Inverse_Iteration import InverseMethod
from Inverse_Iteration_w_shift import InverseShift
import re
import numpy as np
import os
from numpy import linalg as LA
import operator

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


def correctness_test(url, max_urls, func_list):


    url_w = url.replace('.', '_')
    url_w = url_w.replace('/', '')
    url_w = re.sub('https:', '', url_w)
    directory = f"test_result/{url_w}/{max_urls}"
    result_folder_path = os.path.join(THIS_FOLDER, directory)
    stochastic_matrix_file = result_folder_path + "/prepared_matrix.npy"
    M = np.load(stochastic_matrix_file)

    ###########################################
    # correctness test
    f = open(result_folder_path + "/Linalg_page_rank.txt", "w", newline='')
    w, v = LA.eigh(M)
    val_list = w.tolist()
    idx = val_list.index(max(val_list))
    eigenvec_np = v[:,idx]
    f.write(f"dominant eigenvector: {eigenvec_np}")
    # for new funcs
    for func in func_list:
        if func in [qr_Algorithm_GS, qr_Algorithm_HH, shiftedQR_Algorithm]:
            iterations = M.shape[0]
            eigenvec, eigenval = func(M, iterations=iterations)
        else:
            convergence_range = 0.0001
            eigenvec, eigenval = func(M, converge_range=convergence_range, file_path=result_folder_path)

        dist = np.linalg.norm(eigenvec - eigenvec_np)
        f.write(f"\nDistance for np and {func.__name__}: {dist}")

    ###########################################
    f.close()


if __name__ == '__main__':
    url = "https://icerm.brown.edu/"
    max_urls = 30
    func_list = [PowerMethod]
    correctness_test(url, max_urls, func_list)