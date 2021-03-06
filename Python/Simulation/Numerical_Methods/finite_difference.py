import numpy as np;
import scipy.linalg as spla;
from gauss_elimination import gauss_elimination;

def finite_difference(yhist, h, n=1, customge=False):
    '''
    Forward, Central, Backwards finite difference calculation of derivative
    This function uses the Central Finite Difference method to compute the
    derivative for the given data vector. At the ends of the array, central
    difference doesn't work, so the forward difference method and backwards
    difference methods are used instead.
    
    Note that this function decides for you to use forward and bakwards
    differencing functions at either end of the dataset. This cannot be
    turned off or changed.
    
    @arg
    yhist    - M x N numpy.ndarray
               Function value time history, where N is the length of the
               dataset and M is the number different things to take the 
               derivative of. M is usually 1. N corresponds to the number
               of samples in the time history of the dataset.
    h        - double
               Time step
    n        - double (optional)
               Order of finite difference
    customge - bool (optional)
               Specify to use the custom gauss elimination function.
               True to use the function, False use numpy's built in function.
               False by default.
    
    @return
    ydothist - N x M numpy.ndarray
               Finite difference derivative time history
    
    @dependencies
    python 3.6.0
    numpy
    scipy
    
    @author: Matt Marti
    @date: 2019-06-14
    '''

    # Raise Type Errors on bad input
    if type(yhist) != np.ndarray:
        raise TypeError("Argument 'yhist' is not of type numpy.ndarray");
    #
    if type(h) not in [int, float]:
        raise TypeError("Argument 'h' is not of type [int, float]");
    elif type(h) == int:
        h = h + 0.0;
    #
    if type(n) != int:
        raise TypeError("Argument 'n' is not of type int");
    #
    
    # Check yhist shape
    assert n > 0, "Argument 'n' is not greater than zero";
    if yhist.shape.__len__() == 1:
        M = 1;
        yhistold = yhist.copy();
        yhist = np.ndarray((1, yhistold.shape[0]));
        for i in range(0, yhistold.shape[0]):
            yhist[0,i] = yhistold[i];
        #
    else:
        M = yhist.shape[0];
    #
    N = yhist.shape[1];
    assert N >= n+1, 'Not enough data points for given order';
    
    # Preallocate output
    ydothist = np.zeros(yhist.shape, np.float64);
    hmat = np.zeros((n,n), np.float64);
    
    # Forward difference method
    for i in range(0, n):
        
        # Delta t matrix
        for j in range(1, n+1):
            d = 1.0;
            hj = h*j;
            for k in range(1, n+1):
                d = d*k;
                hmat[j-1,k-1] = (hj**k)/d;
            #
        #
        
        # Forward finite difference
        k = 0;
        yfvec = np.ndarray((M, n));
        for j in range(i+1, i+n+1):
            yfvec[:,k] = yhist[:,j] - yhist[:,i];
            k += 1;
        #
        
        # Compute derivative
        if customge:
            ydoti = gauss_elimination(hmat, yfvec.transpose());
        else:
            ydoti = spla.solve(hmat, yfvec.transpose());
        #
        
        # Assign output
        for j in range(ydothist.shape[0]):
            ydothist[j,i] = ydoti[0,j];
        #
    #
    
    # Central difference method
    for i in range( n, N-n ):
        
        # Delta t matrix
        for j in range(1, n+1):
            d = 1.0;
            hj = h*j;
            for k in range(1, n+1):
                d = d*k;
                hmat[j-1,k-1] = (hj**k)/d;
            #
        #
        
        # Forward finite difference
        k = 0;
        yfvec = np.ndarray((M, n));
        for j in range(i+1, i+n+1):
            yfvec[:,k] = yhist[:,j] - yhist[:,i];
            k += 1;
        #
        
        # Backward finite difference
        k = 0;
        ybvec = np.ndarray((M, n));
        for j in range(i-1, i-n-1, -1):
            ybvec[:,k] = yhist[:,i] - yhist[:,j];
            k += 1;
        #
        
        # Compute derivative
        if customge:
            ydoti_f = gauss_elimination(hmat, yfvec.transpose());
            ydoti_b = gauss_elimination(hmat, ybvec.transpose());
            ydoti = 0.5 * (ydoti_f + ydoti_b);
        else:
            ydoti_f = spla.solve(hmat, yfvec.transpose());
            ydoti_b = spla.solve(hmat, ybvec.transpose());
            ydoti = 0.5 * (ydoti_f + ydoti_b);
        #
        
        # Assign output
        for j in range(ydothist.shape[0]):
            ydothist[j,i] = ydoti[0,j];
        #
    #
    
    # Backwards difference method
    for i in range(N-n, N):
        
        # Delta t matrix
        for j in range(1, n+1):
            d = 1.0;
            hj = h*j;
            for k in range(1, n+1):
                d = d*k;
                hmat[j-1,k-1] = (hj**k)/d;
            #
        #
        
        # Backward finite difference
        k = 0;
        ybvec = np.ndarray((M, n));
        for j in range(i-1, i-n-1, -1):
            ybvec[:,k] = yhist[:,i] - yhist[:,j];
            k += 1;
        #
        
        # Compute derivative
        if customge:
            ydoti = gauss_elimination(hmat, ybvec.transpose());
        else:
            ydoti = spla.solve(hmat, ybvec.transpose());
        #
        
        # Assign output
        for j in range(ydothist.shape[0]):
            ydothist[j,i] = ydoti[0,j];
        #
    #
    return ydothist;
#

