## QR Algorithem
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

def qr_Algorithem_HH(x,iterations):
    for _ in range(iterations):
        Q, R = qr_householder(x)
        x = npy.dot(R, Q)       # This update matrix A, by dot product of reverse QR 
        
    eigenvalues = npy.diag(x)  #outputs only the values on the main diaginal
    return eigenvalues


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

def qr_Algorithem(x,iterations):
    for _ in range(iterations):
        Q, R = qr_GS(x)
        x = npy.dot(R, Q)    # This update matrix A, by dot product of reverse QR 
        
    eigenvalues = npy.diag(x)  #outputs only the values on the main diaginal
    return eigenvalues
