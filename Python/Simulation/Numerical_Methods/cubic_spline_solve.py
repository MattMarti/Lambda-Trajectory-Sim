import numpy as np;
import scipy as sp;
import scipy.linalg as spla;

def cubic_spline_solve(xkvec, fkvec, fslope=None, customge=False):
    '''
    Cubic spline interpolation function
    Solves for the parameters that describe a cubic spline. To be used in
    conjunction with "cubicsplineInterp". This function can solve the
    parameters of a cubic spline given data from a vectorized system. For
    example, the three space position of a planet in orbit can be
    interpolated.
    
    @arg
    xkvec         - 1 x n numpy.ndarray
                    Independent variable data points
    fkvec         - m x n numpy.ndarray
                    Dependent variable data points
    fslope        - m x 2 numpy.ndarray (optional)
                    Function slope at boundary points
    customge      - bool (optional)
                    Specify to use the custom gauss elimination function. True
                    to use the function, False use numpy's built in function.
                    False by default.
    
    @return
    splineDataMat - m x n x 5 numpy.ndarray
                    Spline coefficient data matrix. Organized by input data
                    dimension, known value points, and coefficient.
    
    @author: Matt Marti
    @date: 2019-06-16
    '''
    
    # Check boundary condition
    clamped_flag = True;
    if fslope is None:
        clamped_flag = False;
        fslope = np.zeros((fkvec.shape[0],2));
    else:
        if type(fslope) is not np.ndarray:
            raise TypeError('Argument ''fslope'' is not a numpy.ndarray');
        #
        assert fslope.shape[1] is 2, \
            'Argument ''fslope'' does not have the correct number of elements';
        #
    #
    #fslope = fslope.transpose();
    
    # Check type of xkvec
    if type(xkvec) is not np.ndarray:
        raise TypeError('Argument ''xkvec'' is not an numpy.ndarray');
    #
    if (xkvec.shape.__len__() > 1):
        xkvec = np.squeeze(xkvec);
    #
    
    # Check type of fkvec
    if type(fkvec) is not np.ndarray:
        raise TypeError('Argument ''fkvec'' is not an numpy.ndarray');
    #
    if fkvec.shape.__len__() == 1:
        fkvec = fkvec.reshape(1,fkvec.shape[0]);
    #
    assert fkvec.shape[0] == fslope.shape[0], \
        "Argument 'fkvec' and 'fslope' dimensions do not agree";
    #
    
    # Size
    nx = xkvec.shape[0];
    m = fkvec.shape[0];
    
    # Preallocate spline data matrix for output
    splineDataMat = np.zeros((m, nx, 5));
    
    # Build tri-diagonal system of equations
    hkvec = xkvec[1:nx] - xkvec[0:nx-1];
    n = nx - 1;
    H = np.eye(nx);
    for k in range(1,n):
        H[k, k-1] = hkvec[k-1];
        H[k, k] = 2 * ( hkvec[k-1] + hkvec[k] );
        H[k, k+1] = hkvec[k];
    #
    if clamped_flag:
        H[0, 0] = 2*hkvec[0];
        H[0, 1] = hkvec[0];
        H[n, n-1] = hkvec[n-1];
        H[n, n] = 2*hkvec[n-1];
    #
    
    # Generate right hand side
    akvec = fkvec.transpose();
    xstar = np.zeros((nx,m));
    for k in range(1,n):
        xstar[k,:] = 3*( ( akvec[k+1,:] - akvec[k,:] ) / hkvec[k] \
                    - ( akvec[k,:] - akvec[k-1,:] ) / hkvec[k-1] );
    #
    if clamped_flag:
        xstar[0,:] = 3*( (akvec[1,:] - akvec[0,:] )/hkvec[0] - fslope[:,0] );
        xstar[nx-1,:] = 3*( fslope[:,1] - (akvec[nx-1,:] - akvec[nx-2,:] )\
            /hkvec[nx-2] );
        #
    #
    
    # Solve tri-diagonal system of equations
    if customge:
        ckvec = gausselimination(H, xstar);
    else:
        ckvec = spla.solve(H, xstar);
    #
    
    # Compute bkvec and dkvec
    bkvec = np.zeros((nx,m));
    dkvec = np.zeros((nx,m));
    for k in range(0,n):
        bkvec[k,:] = ( akvec[k+1,:] - akvec[k,:] ) / hkvec[k] \
            - hkvec[k] * ( 2*ckvec[k,:] + ckvec[k+1,:] ) / 3;
        dkvec[k,:] = ( ckvec[k+1,:] - ckvec[k,:] ) / ( 3*hkvec[k] );
    #
    bkvec[-1,:] = fslope[:,1].squeeze();
    
    # Assign data vectors to output
    splineDataMat[:,:,0] = akvec.T;
    splineDataMat[:,:,1] = bkvec.T;
    splineDataMat[:,:,2] = ckvec.T;
    splineDataMat[:,:,3] = dkvec.T;
    splineDataMat[0,:,4] = xkvec.squeeze();
    return splineDataMat;
#