import numpy as np

def gauss_elimination(A, B, triflag=False):
    '''
    gauss_elimination.m
    
    Use Gauss Elimination to solve a set of linear equations A*x = b
    Uses partial pivoting to avoid singularities
    
    @arg
    A       - n x n numpy.ndarray
              Matrix that represents the A matrix. Must be square
    B       - n x m numpy.ndarray
              Matrix that represents the set of B vectors
    triflag - bool (optional)
              Flag to return the tridiagonal matrix of A. Default to false
    
    @return
    x_soln  - n x o numpy.ndarray
              Solution matrix to the system of linear equations
    A_aug   - n x n numpy.ndarray
              Upper Triangular Augmented form of input A
    
    @dependencies
    python 3.6.0
    numpy
    
    @author: Matt Marti
    @date: 2019-06-05
    '''
    
    # Raise Type Error if input is not a numpy array
    if type(A) != np.ndarray:
        raise TypeError("Argument 'A' is not of type numpy.ndarray");
    #
    if type(B) != np.ndarray:
        raise TypeError("Argument 'B' is not of type numpy.ndarray");
    #
    
    # Dimension of linear system
    n = A.shape[0]; # Number of A rows
    assert A.shape[0] == A.shape[1], "Argument A is not square matrix";
    assert B.shape[0] == A.shape[1], \
        "Argument 'B' dimension does not match dimension of argument 'A'";
    #
    
    # Copy A and B to local memory
    A_aug = A.copy() + 0.0; # TODO: Figure out how to convert to float
    B_aug = B.copy() + 0.0; # TODO: Figure out how to convert to float
    
    # Gauss Elimination Main Loop
    for i in range( 0, n-1 ): # Iterate by rows
        
        # Pivot zero-valued diagonal elements
        if not A_aug[i,i]:
            k = i + 1;
            successflag = False;
            for k in range( i+1, n ):
                if A[k,i]:
                    Aktemp = A_aug[k,:].copy();
                    A_aug[k,:] = A_aug[i,:];
                    A_aug[i,:] = Aktemp.copy();
                    Bktemp = B_aug[k,:].copy();
                    B_aug[k,:] = B_aug[i,:];
                    B_aug[i,:] = Bktemp.copy();
                    successflag = True;
                    break;
                #
            #
            assert successflag, 'Argument A is singular matrix';
        #
        
        # Perform gauss elimination on this row
        for j in range( i+1, n ): # Iterate by rows
            if A_aug[j,i]: # If there is a non-zero element
                ajioveraii = A_aug[j,i] / A_aug[i,i];
                A_aug[j,:] = A_aug[j,:] - ajioveraii * A_aug[i,:];
                B_aug[j,:] = B_aug[j,:] - ajioveraii * B_aug[i,:];
                #
            #
        #
    #
    
    # Back-substitution loop
    x_soln = np.zeros((n,B.shape[1]));
    for k in range( 0, B.shape[1] ):
        for i in range( n-1, -1, -1 ):
            sum = 0;
            for j in range( i+1, n ):
                sum += A_aug[i,j] * x_soln[j,k];
            #
            x_soln[i,k] = ( B_aug[i,k] - sum ) / A_aug[i,i];
        #
    #
    
    if triflag:
        return x_soln, A_aug;
    else:
        return x_soln;
    #
#

