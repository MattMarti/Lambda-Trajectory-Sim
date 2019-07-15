import unittest;
import numpy as np;
import scipy as sp;
from cubic_spline_fun import cubic_spline_fun;
from cubic_spline_solve import cubic_spline_solve;
from cubic_spline_interp import cubic_spline_interp;

class Test_cubic_spline_interp(unittest.TestCase):
    '''
    Test_cubicsplineInterp
    
    Test case for the cubic spline function. This function just interpolates
    at the given values, given a set of spline data.
    
    @author: Matt Marti
    @date: 2019-06-16
    '''
    
    def test_nominal(self):
        '''Test the spline works for one dimensional case'''
        
        # Given
        f = lambda x : np.sin(x);
        df = lambda x : np.cos(x);
        ddf = lambda x : -np.sin(x);
        xkvec = np.linspace(0, 10, 20);
        fkvec = f(xkvec);
        xinter = np.linspace(0, 10, 1000);
        
        # Generate parameters for clamped boundary conditions
        fslope = np.ndarray((1,2));
        fslope[0,0] = sp.cos(xkvec[0]);
        fslope[0,1] = sp.cos(xkvec[-1]);
        
        # Solve spline
        splineDataMat = cubic_spline_solve( xkvec, fkvec, fslope );
        
        # Run function to interpolate
        dflag = True;
        ddflag = True;
        [finter, dfinter, ddfinter] \
            = cubic_spline_interp( splineDataMat, xinter, dflag, ddflag );
        
        # Test Function values
        fitrue = f(xinter);
        error = fitrue - finter;
        maxerr = np.max(np.abs(error));
        self.assertLess(maxerr, 2.5e-4, 'Spline error too high');
        
        # Test Derivative values
        dfitrue = df(xinter);
        errord = dfitrue - dfinter;
        maxerrd = np.max(np.abs(errord));
        self.assertLess(maxerrd, 1.5e-3, 'Spline derivative error too high');
        
        # Test Derivative values
        ddfitrue = ddf(xinter);
        errordd = ddfitrue - ddfinter;
        maxerrdd = np.max(np.abs(errordd));
        self.assertLess(maxerrdd, 2.5e-2, 'Spline second derivative error too high');
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
        
        # Definition for second derivative function
        def ddfunc(x):
            if type(x) is not np.ndarray:
                ddf = np.zeros((2,1));
            else:
                ddf = np.zeros((2,x.shape[0]));
            #
            ddf[0,:] = -np.sin(x);
            ddf[1,:] = -20;
            return ddf;
        #
        
        # Given
        f = lambda x : func(x);
        df = lambda x : dfunc(x);
        ddf = lambda x : ddfunc(x);
        xkvec = np.linspace(0, 10, 20);
        fkvec = f(xkvec);
        xinter = np.linspace(0, 10, 1000);
        fslope = np.ndarray((2,2)); # Clambed B.C.s
        fslope[:,0] = df(xkvec[0]).squeeze();
        fslope[:,1] = df(xkvec[-1]).squeeze();
        
        # Preallocate truth spline data
        m = 2;
        n = xkvec.shape[0];
        
        # Run new spline
        splineDataMat = cubic_spline_solve( xkvec, fkvec, fslope );
        
        # Run function to interpolate
        dflag = True;
        ddflag = True;
        [finter, dfinter, ddfinter] \
            = cubic_spline_interp( splineDataMat, xinter, dflag, ddflag );
        
        # Compute errors
        error = finter.squeeze() - f(xinter).squeeze();
        errord = dfinter.squeeze() - df(xinter).squeeze();
        errordd = ddfinter.squeeze() - ddf(xinter).squeeze();
        maxerr = np.max(np.abs(error));
        maxerrd = np.max(np.abs(errord));
        maxerrdd = np.max(np.abs(errordd));
        self.assertLess(maxerr, 2.5e-4, 'Spline error too high');
        self.assertLess(maxerrd, 1.5e-3, 'Spline error too high');
        self.assertLess(maxerrdd, 2.5e-2, 'Spline error too high');
    #
    
    def test_out_of_range(self):
        '''Ensure out of bounds checks work'''
    
        # Function handles for function and derivatives
        f = lambda x : sp.sin(x);
        
        # x from 0 to 30 in the correct format
        xkvec = np.linspace(0, 10, 20);
        
        # Generate function values dataset
        fkvec = f(xkvec);
        
        # Generate parameters for clamped boundary conditions
        fslope = np.ndarray((1,2));
        fslope[0,0] = sp.cos(xkvec[0]);
        fslope[0,1] = sp.cos(xkvec[-1]);
        
        # Solve spline
        splineDataMat = cubic_spline_solve( xkvec, fkvec, fslope );
        
        # Run function
        with self.assertRaises(AssertionError):
            cubic_spline_interp(splineDataMat, -0.001);
        with self.assertRaises(AssertionError):
            cubic_spline_interp(splineDataMat, 10.000001);
    #
    
    def test_types(self):
        '''Ensure type checking on inputs works'''
        
        # Given
        f = lambda x : np.sin(x);
        df = lambda x : np.cos(x);
        ddf = lambda x : -np.sin(x);
        xkvec = np.linspace(0, 10, 20);
        fkvec = f(xkvec);
        xinter = np.linspace(0, 10, 1000);
        
        # Generate parameters for clamped boundary conditions
        fslope = np.ndarray((1,2));
        fslope[0,0] = sp.cos(xkvec[0]);
        fslope[0,1] = sp.cos(xkvec[-1]);
        
        # Solve spline
        splineDataMat = cubic_spline_solve( xkvec, fkvec, fslope );
        
        # Run function without errors
        dflag = True;
        ddflag = True;
        finter, dfinter, ddfinter \
            = cubic_spline_interp( splineDataMat, xinter, dflag, ddflag );
        
        # Test with various inputs for splineDataMat
        self.assertRaises(TypeError, cubic_spline_interp, True, xinter);
        self.assertRaises(TypeError, cubic_spline_interp, 0.1, xinter);
        self.assertRaises(TypeError, cubic_spline_interp, "AA", xinter);
        self.assertRaises(TypeError, cubic_spline_interp, 'A', xinter);
        
        # Test with various inputs for xinter
        self.assertRaises(TypeError, cubic_spline_interp, splineDataMat, True);
        self.assertRaises(TypeError, cubic_spline_interp, splineDataMat, "AA");
        self.assertRaises(TypeError, cubic_spline_interp, splineDataMat, 'A');
        
        # Test with various inputs for dflag
        self.assertRaises(TypeError, cubic_spline_interp, splineDataMat, xinter, 0.1);
        self.assertRaises(TypeError, cubic_spline_interp, splineDataMat, xinter, "AA");
        self.assertRaises(TypeError, cubic_spline_interp, splineDataMat, xinter, 'A');
        self.assertRaises(TypeError, cubic_spline_interp, splineDataMat, xinter, xinter);
        
        # Test with various inputs for ddflag
        self.assertRaises(TypeError, cubic_spline_interp, splineDataMat, xinter, True, 0.1);
        self.assertRaises(TypeError, cubic_spline_interp, splineDataMat, xinter, True, "AA");
        self.assertRaises(TypeError, cubic_spline_interp, splineDataMat, xinter, True, 'A');
        self.assertRaises(TypeError, cubic_spline_interp, splineDataMat, xinter, True, xinter);
    #
#