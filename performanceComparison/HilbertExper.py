from scipy.linalg import hilbert
from efficient_eigensolvers import PowerMethod, QR_shifted, QR_unshifted, RayleighQuotientIteration
from matricesGenerator import matrix_generator
import numpy as np
import scipy

def Hilbert_test(dim):
    A = hilbert(dim)
    B, vals = matrix_generator(dim)
    eigenvec, eigenval, iterations = QR_shifted(A)

    print(iterations)
    residue = np.linalg.norm(A.dot(eigenvec) - eigenval * eigenvec)
    print(residue)
    eigenvals, eigenvecs = np.linalg.eigh(A)
    eigenvals = eigenvals.tolist()
    idx = eigenvals.index(max(eigenvals))
    eigenvec_np = eigenvecs[:, idx]
    eigenvec_np = eigenvec_np / np.linalg.norm(eigenvec_np)
    dist = np.linalg.norm(eigenvec_np - eigenvec)
    print(dist)

    eigenvec,eigenval,iterations = QR_shifted(B)
    print(iterations)
    residue = np.linalg.norm(B.dot(eigenvec) - eigenval * eigenvec)
    print(residue)
    eigenvals, eigenvecs = np.linalg.eig(B)
    eigenvals = eigenvals.tolist()
    idx = eigenvals.index(max(eigenvals))
    eigenvec_np = eigenvecs[:, idx]
    eigenvec_np = eigenvec_np / np.linalg.norm(eigenvec_np)
    dist = np.linalg.norm(eigenvec_np - eigenvec)
    print(dist)


if __name__ == '__main__':
    Hilbert_test(12)
