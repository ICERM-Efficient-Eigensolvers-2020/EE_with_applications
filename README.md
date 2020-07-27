# Design notes

## **Part I: Power Iteration Method Implementation**

###### ***Power Iteration***

`def _PowerMethod_ (matrix: A, int: norm_indicator, float: terminate_range)       
 `   
     
 - Effect: Produce a sequence of vectors that converges to an eigenvector corresponding to the largest eigenvalue of input matrix A
            
- Input: square matrix A, normalize indicator, termination range
	
- Output: dominant eigenvalue and its corresponding eigenvector 

- Pseudocode:
		
        1. initialize a unit vector v_0 with n*1
        2. calculate v_0 Rayleigh Quotient \lambda_0 by \lambda = v^T * A^T v / (v^T * v)
        3. while not reach convergence condition
                update new vector: v_k = A * v_{k-1}
                (optional) normalize: v_k = v_k / norm(v_k)
                update Rayleigh Quotient: \lambda_k = v_k ^ T * A * v_k
                convergence condition: |\lambda_k - \lambda_{k-1}|
           
        4. return v_k, \lambda_k

 ###### ****Converge Process Print :**** 
 
`` def print_log(index, eigenvector_list, eigenvalue_list, err_list)``
    
    
    
## **Part II: Page Rank Algorithm**

We are calculating the limiting probability distribution of webpages utilizing power method, which is similar to the Markov Process.
    
With one thing in mind, 1.0 is the largest eigenvalue for the probability transmission matrix A. (proof)
    
###### ***Page Rank without Dangling Nodes*** 
    
`def PageRank(diGraph, weight)`
    
- Effect: calculate the limiting distribution of this random walk

- Input: DiGraph

- Output: importance score


- Pseudocode:


        1. Check whether this graph is connnected
        
        2. Compute the link matrix A and weighted matrix M:
            A[i][j] = v_{ij} 
      
        3. Call PowerMethod to get the dominant eigenvector.
  
    
 

## **Part III: QR Algorithm**

The QR algorithm is a program that works to calculate the eigenvalues and eigenvectors of a matrix.

###### ***QR Decomposition***
- Effect: Produce two matricies whose produce equals the inputted matrix A 
            
- Input: square matrix A, normalize indicator
	
- Output: Q and R matricies 

###### ***The Gram-Schmidt process***
This method implements the modified Gram-Schmidt (GS) process. The modified GS subtracts one projection at a time verses the standard GS that subtracts all projections at once.

###### ***The Householder transformations***

###### ***Shifted QR decomposition***



## **Part IV: Inverse Power Iteration Method Implementation**

###### ***Inverse Iteration***

`def _InverseMethod_ (matrix: A, float: converge_range)`   
     
- Effect: Produce a sequence of vectors that converges to an eigenvector corresponding to the eigenvalue of smallest magnitude of input matrix A
            
- Input: square matrix A, convergence range
	
- Output: smallest eigenvalue and its corresponding eigenvector

- Pseudocode:
		
        1. initialize a unit vector v_0 with n*1
        2. let \lambda_0 = v_0 * A * v_0
        3. while not reach convergence condition
                update new vector: Solve A(v_k) = v_(k-1) for v_k
                normalize: v_k = v_k / norm(v_k)
                update lambda: \lambda_k = v_k * A * v_k
                convergence condition: |\lambda_k - \lambda_{k-1}|
           
        4. return v_k, \lambda_k

 ###### ****Converge Process Print :**** 
 
`` def print_log(index, eigenvector_list, eigenvalue_list, err_list)``


###### ***Inverse Iteration with Shift***

`def _InverseMethod_ (matrix: A, float: mu, float: converge_range)`   
     
- Effect: Produce a sequence of vectors that converges to an eigenvector corresponding to the eigenvalue input matrix A that is closest to the chosen shift
            
- Input: square matrix A, shift mu, convergence range
	
- Output: eigenvalue closest to mu and its corresponding eigenvector

- Pseudocode:

initialize a unit vector v_0 with n*1
      
        1. initialize a unit vector v_0 with n*1
        2. let \lambda_0 = v_0 * A * v_0
        3. let B = (A - \mu * I)
	4. while not reach convergence condition
                update new vector: Solve B(v_k) = v_(k-1) for v_k
                normalize: v_k = v_k / norm(v_k)
                update lambda: \lambda_k = v_k * A * v_k
                convergence condition: |\lambda_k - \lambda_{k-1}|
        5. return v_k, \lambda_k

 ###### ****Converge Process Print :**** 
 
`` def print_log(index, eigenvector_list, eigenvalue_list, err_list)``
