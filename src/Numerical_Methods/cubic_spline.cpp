
#include "cubic_spline.h"

def cubic_spline_fun(xkvec, fkvec, xinter, fslope=None, customge=False):
    '''
    Cubic spline interpolation function
    Interpolates function values at specified points using a cubic spline
    
    @arg
    xkvec    - n x 1 numpy.ndarray
               Independent variable data points
    fkvec    - n x 1 numpy.ndarray
               Dependent variable data points
    xinter   - n x 1 numpy.ndarray
               Interpolation points
    fslope   - 2 x 1 numpy.ndarray (Optional)
               Function slope at boundary points
    customge - bool (optional)
               Specify to use the custom gauss elimination function.
               True to use the function, False use numpy's built in function.
               False by default.
    
    @return
    finter   - n x 1 numpy.ndarray
               Interpolated function value
    dfinter  - n x 1 numpy.ndarray
               Interpolated function derivative value
    akvec    - n x 1 numpy.ndarray
               Spline coefficient vector: a
    bkvec    - n x 1 numpy.ndarray
               Spline coefficient vector: b
    ckvec    - n x 1 numpy.ndarray
               Spline coefficient vector: c
    dkvec    - n x 1 numpy.ndarray
               Spline coefficient vector: d
    xstar    - n x 1 numpy.ndarray
               Intermediate solution in tri-diagonal equations
    
    @dependencies
    python 3.6.0
    numpy
    scipy
    
    @author: Matt Marti
    @date: 2019-06-15
    '''
    
    # Check boundary condition
    clamped_flag = True;
    if fslope is None:
        clamped_flag = False;
        fslope = np.zeros((2,1));
    else:
        if type(fslope) is not np.ndarray:
            raise TypeError('Argument ''fslope'' is not a numpy.ndarray')
        #
        if (fslope.shape.__len__() > 1):
            fslope = fslope.squeeze();
        #
        assert fslope.shape[0] is 2, \
            'Argument ''fslope'' does not have the correct number of elements'
    #
    
    # Check dimension of xkvec
    if type(xkvec) is not np.ndarray:
        raise TypeError('Argument ''xkvec'' is not an numpy.ndarray');
    #
    if (xkvec.shape.__len__() > 1):
        xkvec = xkvec.squeeze();
    #
    
    # Check dimension of fkvec
    if type(fkvec) is not np.ndarray:
        raise TypeError('Argument ''fkvec'' is not an numpy.ndarray');
    #
    if (fkvec.shape.__len__() > 1):
        fkvec = fkvec.squeeze();
    #
    
    # Check dimension of xinter
    if type(xinter) not in [np.ndarray, int, float]:
        raise TypeError('Argument ''xinter'' is not an numpy.ndarray');
    #
    if (type(xinter) in [int, float]):
        xinter = np.zeros((1,1)) + xinter;
    elif (xinter.shape.__len__() > 1):
        xinter = xinter.squeeze();
    #
    
    # Size
    nx = xkvec.shape[0];
    
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
    akvec = fkvec;
    xstar = np.zeros((nx,1));
    for k in range(1,n):
        xstar[k] = 3*( ( akvec[k+1] - akvec[k] ) / hkvec[k] \
                    - ( akvec[k] - akvec[k-1] ) / hkvec[k-1] );
    #
    if clamped_flag:
        xstar[0] = 3*( (akvec[1] - akvec[0] )/hkvec[0] - fslope[0] );
        xstar[nx-1] = 3*( fslope[1] - (akvec[nx-1] - akvec[nx-2] )/hkvec[nx-2] );
    #
    
    # Solve tri-diagonal system of equations
    if customge:
        ckvec = gausselimination(H, xstar);
    else:
        ckvec = spla.solve(H, xstar);
    #
    
    # Compute bkvec and dkvec
    bkvec = np.zeros((nx,1));
    dkvec = np.zeros((nx,1));
    for k in range(0,n):
        bkvec[k] = ( akvec[k+1] - akvec[k] ) / hkvec[k] \
            - hkvec[k] * ( 2*ckvec[k] + ckvec[k+1] ) / 3;
        dkvec[k] = ( ckvec[k+1] - ckvec[k] ) / ( 3*hkvec[k] );
    #
    bkvec[-1] = fslope[1];
    
    # Interpolate function
    finter = np.zeros((1,xinter.shape[0]));
    dfinter = np.zeros((1,xinter.shape[0]));
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
            finter[0,i] = akvec[-1];
            dfinter[0,i] = bkvec[-1];
            continue;
        #
        
        # Spline interpolation
        hi = xinter[i] - xkvec[k];
        finter[0,i] = akvec[k] + bkvec[k]*hi + ckvec[k]*hi**2 + dkvec[k]*hi**3;
        dfinter[0,i] = bkvec[k] + 2*ckvec[k]*hi + 3*dkvec[k]*hi**2;
    #
    
    return finter, dfinter, akvec, bkvec, ckvec, dkvec
#