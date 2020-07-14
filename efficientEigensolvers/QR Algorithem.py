## QR Algorithm
# Author: Kelly Rivera

# This code is an implementation of a PageRank Algorithm variant using QR Decomposition
# Implementing Householder and Gram-Schmidt Process

### Import Libraries
import numpy as npy
import scipy as sp
import scipy.linalg as spl  # SciPy Linear Algebra Library
import matplotlib.pyplot as plt


### Householder transformation method
def qr_householder(x):
    Q, R = npy.linalg.qr(x)
    return Q, R 

def qr_Algorithm_HH(x,iterations):
    m, n = x.shape
    Q_last = npy.identity(n)
    for _ in range(iterations):
        Q, R = qr_householder(x)
        # This update matrix A, by dot product of reverse QR 
        x = npy.dot(R, Q) 
        
        eigenvectors = npy.dot(Q_last, Q)
        Q_last = eigenvectors
        
    eigenvalues = npy.diag(x)  #outputs only the values on the main diaginal
    return eigenvalues, eigenvectors


### Gram-Schmidt Process
def qr_GS(x):
    m, n = x.shape
    Q = npy.zeros((m, n)) # Q is all zero
    R = npy.zeros((n, n))

    for j in range(n): 
        v = x[:, j] # x[:,0] returns the first* column* of x, x[:,1] reutrns the second column etc

        for i in range(j): 
            q = Q[:, i]    
            R[i, j] = q.dot(v)
            v = v - R[i, j] * q

        vNorm = npy.linalg.norm(v)
        R[j, j] = vNorm
        Q[:, j] = v / vNorm
   
    return Q, R

def qr_Algorithm(x,iterations):
    m, n = x.shape
    Q_last = npy.identity(n)
    for _ in range(iterations):
        Q, R = qr_GS(x)
        # This update matrix A, by dot product of reverse QR 
        x = npy.dot(R, Q) 
        
        eigenvectors = npy.dot(Q_last, Q)
        Q_last = eigenvectors
    eigenvalues = npy.diag(x)  #outputs only the values on the main diaginal
    return eigenvalues, eigenvectors


### QR Gram-Schmidt with Shift 
def shiftedQR_Algorithm(x, iterations):
    m, n = x.shape
    I = npy.identity(n)
    Q_last = npy.identity(n)
    
    for _ in range(iterations):
        μ = x[[n-1],[n-1]]         # shift: μ = a_nn
        Q, R = qr_GS((x - (μ*I)))  # A − μI = QR: preforms the gram schmidt process with shift
                                     
        x = npy.dot(R,Q) + (μ*I)   # This update matrix A, by dot product of reverse QR and adding back the shift
        
        eigenvectors = npy.dot(Q_last, Q)
        Q_last = eigenvectors
        
    eigenvalues = npy.diag(x)  #outputs only the values on the main diaginal
    return eigenvalues, eigenvectors 
