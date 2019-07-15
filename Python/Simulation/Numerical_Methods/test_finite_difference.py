import unittest;
import math;
import numpy as np;
from finite_difference import finite_difference;

class Test_finite_difference(unittest.TestCase):
    '''
    Test_finite_difference
    
    Test case for the finite difference function
    
    @dependencies
    python 3.6.0
    unittest
    numpy
    
    @author: Matt Marti
    @date: 2019-06-14
    '''
    
    def test_nominal_01(self):
        '''Make sure all the orders work'''
        
        # Function input
        h = 0.1;
        trange = np.arange(0, 10+h, h);
        thist = np.zeros((1,trange.shape[0])); # t = (0:h:10)'
        for i in range(0, trange.shape[0]):
            thist[0,i] = trange[i];
        #
        yhist = (-9.81/2)*thist**2 + 50*thist + 200;
        
        # Truth value
        ydottruthhist = -9.81*thist + 50;
        
        # Test Function call
        errvec = [5e-1, 1e-11, 1e-11, 1e-11, 1e-11, 1.1e-11, 2e-11, 3e-11, 5e-11];
        for n in range(1, 10):
            
            # Function call
            [ydothist] = finite_difference(yhist, h, n);
            
            # Compute maximum absolute error
            errhist = ydothist - ydottruthhist;
            maxerr = np.max(np.abs(errhist));
            self.assertLess(maxerr, errvec[n-1], \
                "Error for " + str(n) + " order polynomial is too high")
            #
        #
    #
    
    def test_nominal_02(self):
        '''Derivative of nonlinear function is approximate and all orders work
        Also test that multiple data entries work'''
        
        # Create time array
        h = .1;
        t = np.arange(0, 10+h, h); # t = (0:h:10)'
        thist = np.zeros((1, t.shape[0]));
        for i in range(0, t.shape[0]):
            thist[0,i] = t[i];
        #
        
        # Create function values to differentiate
        sinvec = np.sin(thist);
        cosvec = np.cos(thist);
        yhist = np.zeros((2, t.shape[0]));
        yhist[0,:] = sinvec.copy();
        yhist[1,:] = cosvec.copy();
        
        # Truth value
        ydottruthhist = np.zeros((2, t.shape[0]));
        ydottruthhist[0,:] = cosvec.copy();
        ydottruthhist[1,:] = - sinvec.copy();
        
        # Test Function call
        errvec = [5e-1, 5e-3, 2.5e-4, 2.5e-5, 2e-6, 2e-7, 2e-8, 2e-9, 2e-10];
        for n in range(1, 10):
            
            # Function call
            ydothist = finite_difference(yhist, h, n);
            
            # Compute maximum absolute error
            errhist = ydothist - ydottruthhist;
            maxerr = np.max(np.abs(errhist));
            self.assertLess(maxerr, errvec[n-1], \
                "Error for " + str(n) + " order polynomial is too high")
            #
        #
    #
    
    def test_default_n_value(self):
        '''Ensure that n is chosen by default if not specified'''
        
        # Function input
        h = 0.1;
        trange = np.arange(0, 10+h, h);
        thist = np.zeros((1,trange.shape[0])); # t = (0:h:10)'
        for i in range(0, trange.shape[0]):
            thist[0,i] = trange[i];
        #
        yhist = (-9.81/2)*thist**2 + 50*thist + 200;
        
        # Truth value
        ydottruthhist = -9.81*thist + 50;
        
        # Test Function call
        [ydothist] = finite_difference(yhist, h);
        
        # Compute maximum absolute error
        errhist = ydothist - ydottruthhist;
        maxerr = np.max(np.abs(errhist));
        
        # Assert max absolute error is within bounds
        self.assertLess(maxerr, 5e-1, \
            "Error for default order polynomial is too high")
        self.assertGreater(maxerr, 1e-1, \
            "Error for default order polynomial is too low")
        #
    #
    
    def test_customge(self):
        '''Ensure that if specified, the custom gauss_elimination function is 
        used'''
        
        # Function input
        h = 0.1;
        trange = np.arange(0, 10+h, h);
        thist = np.zeros((1,trange.shape[0])); # t = (0:h:10)'
        for i in range(0, trange.shape[0]):
            thist[0,i] = trange[i];
        #
        yhist = (-9.81/2)*trange**2 + 50*trange + 200;
        
        # Truth value
        ydottruthhist = -9.81*thist + 50;
        
        # Test Function call
        [ydothist] = finite_difference(yhist, h, 1, True);
        
        # Compute maximum absolute error
        errhist = ydothist - ydottruthhist;
        maxerr = np.max(np.abs(errhist));
        
        # Assert max absolute error is within bounds
        self.assertLess(maxerr, 5e-1, \
            "Error for default order polynomial is too high")
        self.assertGreater(maxerr, 1e-1, \
            "Error for default order polynomial is too low")
        #
    #
    
    def test_types(self):
        '''Make sure the function only works on numpy.ndarrays'''
        
        # Function input
        h = 0.1;
        trange = np.arange(0, 10+h, h);
        thist = np.zeros((1,trange.shape[0])); # t = (0:h:10)'
        for i in range(0, trange.shape[0]):
            thist[0,i] = trange[i];
        #
        yhist = (-9.81/2)*thist**2 + 50*thist + 200;
        
        # Truth value
        ydottruthhist = -9.81*thist + 50;
        
        # Test with various inputs for yhist
        self.assertRaises(TypeError, finite_difference, 0.0, h, 1);
        self.assertRaises(TypeError, finite_difference, True, h, 1);
        self.assertRaises(TypeError, finite_difference, "AAA", h, 1);
        self.assertRaises(TypeError, finite_difference, 'A', h, 1);
        
        # Test with various inputs for h
        self.assertRaises(TypeError, finite_difference, yhist, True, 1);
        self.assertRaises(TypeError, finite_difference, yhist, "AAA", 1);
        self.assertRaises(TypeError, finite_difference, yhist, 'A', 1);
        self.assertRaises(TypeError, finite_difference, yhist, yhist, 1);
        
        # Test with various inputs for n
        self.assertRaises(TypeError, finite_difference, yhist, h, True);
        self.assertRaises(TypeError, finite_difference, yhist, h, 0.1);
        self.assertRaises(TypeError, finite_difference, yhist, h, yhist);
        self.assertRaises(TypeError, finite_difference, yhist, h, "AAA");
        self.assertRaises(TypeError, finite_difference, yhist, h, 'A');
    #
#

