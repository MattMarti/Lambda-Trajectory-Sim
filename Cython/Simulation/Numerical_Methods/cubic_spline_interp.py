import numpy as np;

def cubic_spline_interp( splineDataMat, xinter, dflag=False, ddflag=False ):
    '''
    Cubic spline interpolation function
    Interpolates function values at specified points using data from a solved
    cubic spline. To be used in conjunction with "cubicsplineSolve.m".
    
    @arg
    splineDataMat - m x n x 5 numpy.ndarray
                    Spline coefficient data matrix. Organized by input data
                    dimension, known value points, and coefficient.
    xinter        - 1 x n numpy.ndarray
                    Interpolation points
    dflag         - bool (optional)
                    Optional flag to make the function return the derivative.
                    False by default.
    ddflag        - bool (optional)
                    Optional flag to make the function return the second 
                    derivative of the interpolated function. False by 
                    default.
    
    @return
    finter        - n x 1 numpy.ndarray
                    Interpolated function value
    dfinter       - n x 1 numpy.ndarray
                    Interpolated function derivative value
    ddfinter      - n x 1 numpy.ndarray
                    Interpolated function second derivative value
    
    @author: Matt Marti
    @date: 2019-06-16
    '''
    
    # Check type of splineDataMat
    if type(splineDataMat) is not np.ndarray:
        raise TypeError('Argument ''splineDataMat'' is not an numpy.ndarray');
    #
    
    # Check type of xinter
    if type(xinter) not in [np.ndarray, int, float]:
        raise TypeError('Argument ''xinter'' is not an numpy.ndarray');
    #
    
    # Check type of dflag
    if type(dflag) is not bool:
        raise TypeError('Argument ''dflag'' is not a bool');
    #
    
    # Check type of ddflag
    if type(ddflag) is not bool:
        raise TypeError('Argument ''ddflag'' is not a bool');
    #
    
    # Check dimension of xinter
    if (type(xinter) in [int, float]):
        xinter = np.zeros((1,1)) + xinter;
    elif (xinter.shape.__len__() > 1):
        xinter = xinter.squeeze();
    #
    
    # Size
    m = splineDataMat.shape[0];
    nx = splineDataMat.shape[1];
    
    # Preallocate output
    finter = np.zeros((m,xinter.shape[0]));
    if dflag:
        dfinter = np.zeros((m,xinter.shape[0]));
    #
    if ddflag:
        ddfinter = np.zeros((m,xinter.shape[0]));
    #
    
    # Partition a, b, c, d coefficients
    akvec = splineDataMat[:,:,0].reshape(m,nx);
    bkvec = splineDataMat[:,:,1].reshape(m,nx);
    ckvec = splineDataMat[:,:,2].reshape(m,nx);
    dkvec = splineDataMat[:,:,3].reshape(m,nx);
    xkvec = splineDataMat[0,:,4].squeeze();
    
    # Interpolate function
    for i in range(0, xinter.shape[0]):
        
        # Check that interpolated value is within function range
        assert xinter[i] >= xkvec[0] and xinter[i] <= xkvec[-1], \
            'Interpolation value not within bounds';
        
        # Find x value just below xinter(i)
        k = 1;
        while k < nx:
            if xinter[i] < xkvec[k]:
                k = k - 1;
                break;
            #
            assert k <= xkvec.shape[0], "Indexing value too high";
            k = k + 1;
        #
        if k >= nx: # Point is on upper boundary
            finter[:,i] = akvec[:,-1];
            if dflag:
                dfinter[:,i] = bkvec[:,-1];
            #
            if ddflag:
                ddfinter[:,i] = 2*ckvec[:,-1];
            #
            continue;
        #
        
        # Spline interpolation
        hi = xinter[i] - xkvec[k];
        finter[:,i] = akvec[:,k] + bkvec[:,k]*hi + ckvec[:,k]*hi**2 + dkvec[:,k]*hi**3;
        if dflag:
            dfinter[:,i] = bkvec[:,k] + 2*ckvec[:,k]*hi + 3*dkvec[:,k]*hi**2;
        #
        if ddflag:
            ddfinter[:,i] = 2*ckvec[:,k] + 6*dkvec[:,k]*hi;
        #
    #
    
    # Return
    if dflag:
        if ddflag:
            return finter, dfinter, ddfinter;
        else:
            return finter, dfinter;
        #
    else:
        return finter;
    #
#