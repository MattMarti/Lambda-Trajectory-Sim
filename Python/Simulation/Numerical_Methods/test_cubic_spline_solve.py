import unittest;
import numpy as np;
import scipy as sp;
from cubic_spline_solve import cubic_spline_solve;
from cubic_spline_fun import cubic_spline_fun;

class Test_cubic_spline_solve(unittest.TestCase):
    '''
    Test_cubicsplineSolve
    
    Test case for the cubic spline solver function. This function just solves
    for the spline data, so that the spline can be precomputed before code is
    run. This improves code performance by removing the need to invert a
    matrix every time the spline function is called.
    
    @author: Matt Marti
    @date: 2019-06-16
    '''
    
    def test_nominal_01(self):
        '''Test the spline solve for nominal test case'''
        
        # Function handles for function and derivatives
        f = lambda x : sp.sin(x);
        df = lambda x : sp.cos(x);
        
        # x from 0 to 30 in the correct format
        xrange = np.linspace(0, 10, 20);
        xkvec = np.zeros((1, xrange.shape[0]));
        for i in range(0, xrange.shape[0]):
            xkvec[0,i] = xrange[i];
        #
        
        # Generate function values dataset
        fkvec = f(xkvec);
        xinter = np.linspace(0, 10, 1000);
        
        # Generate parameters for clamped boundary conditions
        fslope = np.ndarray((1,2));
        fslope[0,0] = sp.cos(xkvec[0,0]);
        fslope[0,1] = sp.cos(xkvec[0,-1]);
        
        # Compute already tested spline
        _, _, akvec, bkvec, ckvec, dkvec \
            = cubic_spline_fun(xkvec, fkvec, xinter, fslope);
        splineDataTrue = np.zeros((1, xkvec.shape[1], 5));
        splineDataTrue[0,:,0] = akvec.squeeze();
        splineDataTrue[0,:,1] = bkvec.squeeze();
        splineDataTrue[0,:,2] = ckvec.squeeze();
        splineDataTrue[0,:,3] = dkvec.squeeze();
        splineDataTrue[0,:,4] = xkvec.squeeze();
        
        # Run spline solve
        splineDataMat = cubic_spline_solve( xkvec, fkvec, fslope );
        
        # Test Function truth values
        error = splineDataMat - splineDataTrue;
        maxerr = np.max(np.abs(error));
        self.assertLess(maxerr, 1e-12, 'Spline error too high');
    #
    
    def test_multiple_01(self):
        '''Test the spline works for a two dimensional case'''
        
        # Definition for two dimensional function output
        def func(x):
            if type(x) is not np.ndarray:
                f = np.zeros((2,1));
            else:
                f = np.zeros((2,x.shape[0]));
            #
            f[0,:] = np.sin(x);
            f[1,:] = -10*x**2 + 50*x + 1000;
            return f;
        #
        
        # Definition for derivative function
        def dfunc(x):
            if type(x) is not np.ndarray:
                df = np.zeros((2,1));
            else:
                df = np.zeros((2,x.shape[0]));
            #
            df[0,:] = np.cos(x);
            df[1,:] = -20*x + 50;
            return df;
        #
        
        # Given
        f = lambda x : func(x);
        df = lambda x : dfunc(x);
        xkvec = np.linspace(0, 10, 20);
        fkvec = f(xkvec);
        xinter = np.linspace(0, 10, 1000);
        fslope = np.ndarray((2,2)); # Clambed B.C.s
        fslope[:,0] = df(xkvec[0]).squeeze();
        fslope[:,1] = df(xkvec[-1]).squeeze();
        
        # Preallocate truth spline data
        m = 2;
        n = xkvec.shape[0];
        splineDataTrue = np.zeros((m, n, 5));
        splineDataTrue[0,:,4] = xkvec;
        
        # Run true spline for first dataset
        _, _, akvec, bkvec, ckvec, dkvec \
            = cubic_spline_fun(xkvec, fkvec[0,:], xinter, fslope[0,:]);
        splineDataTrue[0,:,0] = akvec.squeeze();
        splineDataTrue[0,:,1] = bkvec.squeeze();
        splineDataTrue[0,:,2] = ckvec.squeeze();
        splineDataTrue[0,:,3] = dkvec.squeeze();
        
        # Run true spline for second dataset
        _, _, akvec, bkvec, ckvec, dkvec \
            = cubic_spline_fun(xkvec, fkvec[1,:], xinter, fslope[1,:]);
        splineDataTrue[1,:,0] = akvec.squeeze();
        splineDataTrue[1,:,1] = bkvec.squeeze();
        splineDataTrue[1,:,2] = ckvec.squeeze();
        splineDataTrue[1,:,3] = dkvec.squeeze();
        
        # Run new spline
        splineDataMat = cubic_spline_solve( xkvec, fkvec, fslope );
        
        # Test Function truth values
        error = splineDataMat - splineDataTrue;
        maxerr = np.max(np.abs(error));
        self.assertLess(maxerr, 1e-12, 'Spline error too high');
    #
    
    def test_types(self):
        '''Test that the function raises type errors on bad input'''
        
        # Function handles for function and derivatives
        f = lambda x : sp.sin(x);
        df = lambda x : sp.cos(x);
        
        # x from 0 to 30 in the correct format
        xrange = np.linspace(0, 10, 20);
        xkvec = np.zeros((1, xrange.shape[0]));
        for i in range(0, xrange.shape[0]):
            xkvec[0,i] = xrange[i];
        #
        
        # Generate function values dataset
        fkvec = f(xkvec);
        xinter = np.linspace(0, 10, 1000);
        
        # Generate parameters for clamped boundary conditions
        fslope = np.ndarray((1,2));
        fslope[0,0] = sp.cos(xkvec[0,0]);
        fslope[0,1] = sp.cos(xkvec[0,-1]);
        
        # Run function without errors
        splineDataMat = cubic_spline_solve( xkvec, fkvec, fslope );
        
        # Test with various inputs for xkvec
        self.assertRaises(TypeError, cubic_spline_solve, True, fkvec, fslope);
        self.assertRaises(TypeError, cubic_spline_solve, 0.1, fkvec, fslope);
        self.assertRaises(TypeError, cubic_spline_solve, "AA", fkvec, fslope);
        self.assertRaises(TypeError, cubic_spline_solve, 'A', fkvec, fslope);
        
        # Test with various inputs for xkvec
        self.assertRaises(TypeError, cubic_spline_solve, xkvec, True, fslope);
        self.assertRaises(TypeError, cubic_spline_solve, xkvec, 0.1, fslope);
        self.assertRaises(TypeError, cubic_spline_solve, xkvec, "AA", fslope);
        self.assertRaises(TypeError, cubic_spline_solve, xkvec, 'A', fslope);
        
        # Test with various inputs for fslope
        self.assertRaises(TypeError, cubic_spline_solve, xkvec, fkvec, True);
        self.assertRaises(TypeError, cubic_spline_solve, xkvec, fkvec, 0.1);
        self.assertRaises(TypeError, cubic_spline_solve, xkvec, fkvec, "AA");
        self.assertRaises(TypeError, cubic_spline_solve, xkvec, fkvec, 'A');
    #
#