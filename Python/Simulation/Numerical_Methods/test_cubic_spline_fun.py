import unittest;
import numpy as np;
import scipy as sp;
from cubic_spline_fun import cubic_spline_fun;

class Test_cubic_spline_fun(unittest.TestCase):
    '''
    Test_cubic_spline
    
    Test case for the cubic spline function. Based on the driver script for
    the solution to AOE 4404 Assignment 5, problems 1 to 3. Cubic spline and
    Lagrange interpolation.
    
    @dependencies
    python 3.6.0
    numpy
    scipy
    
    @author: Matt Marti
    @date: 2019-06-15
    '''
    
    def test_nominal_csfun(self):
        '''Ensure nominal function works'''
    
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
        fslope = np.ndarray((2,1));
        fslope[0,0] = sp.cos(xkvec[0,0]);
        fslope[1,0] = sp.cos(xkvec[0,-1]);
        
        # Run function
        [finter, dfinter, akvec, bkvec, ckvec, dkvec] \
            = cubic_spline_fun(xkvec, fkvec, xinter, fslope);
        
        # Obtain Function and Derivative truth values
        fitrue = f(xinter);
        dfitrue = df(xinter);
        
        # Compute maximum absolute error
        err_f_hist = finter.squeeze() - fitrue.squeeze();
        err_df_hist = dfinter.squeeze() - dfitrue.squeeze();
        max_f_err = np.max(np.abs(err_f_hist));
        max_df_err = np.max(np.abs(err_df_hist));
        
        # Assert max absolute error is within bounds
        self.assertLess(max_f_err, 2.5e-4, \
            "Error for interpolated function values too high")
        self.assertLess(max_df_err, 1.5e-3, \
            "Error for interpolated function values too high")
        #
    #
    
    def test_out_of_range_csfun(self):
        '''Ensure out of bounds checks work'''
    
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
        fslope = np.ndarray((2,1));
        fslope[0,0] = sp.cos(xkvec[0,0]);
        fslope[1,0] = sp.cos(xkvec[0,-1]);
        
        # Run function
        with self.assertRaises(AssertionError):
            cubic_spline_fun(xkvec, fkvec, -0.001, fslope);
        with self.assertRaises(AssertionError):
            cubic_spline_fun(xkvec, fkvec, 10.000001, fslope);
    #
    
    def test_types_csfun(self):
        '''Ensure type checking on inputs works'''
    
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
        fslope = np.ndarray((2,1));
        fslope[0,0] = sp.cos(xkvec[0,0]);
        fslope[1,0] = sp.cos(xkvec[0,-1]);
        
        # Run function without errors
        [finter, dfinter, akvec, bkvec, ckvec, dkvec] \
            = cubic_spline_fun(xkvec, fkvec, xinter, fslope);
        
        # Test with various inputs for xkvec
        self.assertRaises(TypeError, cubic_spline_fun, True, fkvec, xinter, fslope);
        self.assertRaises(TypeError, cubic_spline_fun, 0.1, fkvec, xinter, fslope);
        self.assertRaises(TypeError, cubic_spline_fun, "AA", fkvec, xinter, fslope);
        self.assertRaises(TypeError, cubic_spline_fun, 'A', fkvec, xinter, fslope);
        
        # Test with various inputs for xkvec
        self.assertRaises(TypeError, cubic_spline_fun, xkvec, True, xinter, fslope);
        self.assertRaises(TypeError, cubic_spline_fun, xkvec, 0.1, xinter, fslope);
        self.assertRaises(TypeError, cubic_spline_fun, xkvec, "AA", xinter, fslope);
        self.assertRaises(TypeError, cubic_spline_fun, xkvec, 'A', xinter, fslope);
        
        # Test with various inputs for xinter
        self.assertRaises(TypeError, cubic_spline_fun, xkvec, fkvec, True, fslope);
        self.assertRaises(TypeError, cubic_spline_fun, xkvec, fkvec, "AA", fslope);
        self.assertRaises(TypeError, cubic_spline_fun, xkvec, fkvec, 'A', fslope);
        
        # Test with various inputs for fslope
        self.assertRaises(TypeError, cubic_spline_fun, xkvec, fkvec, xinter, True);
        self.assertRaises(TypeError, cubic_spline_fun, xkvec, fkvec, xinter, 0.1);
        self.assertRaises(TypeError, cubic_spline_fun, xkvec, fkvec, xinter, "AA");
        self.assertRaises(TypeError, cubic_spline_fun, xkvec, fkvec, xinter, 'A');
    #
#