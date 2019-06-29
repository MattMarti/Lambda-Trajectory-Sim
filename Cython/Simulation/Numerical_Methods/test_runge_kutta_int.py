import unittest;
import math;
import numpy as np;
import scipy as sp;
from runge_kutta_int import runge_kutta_int;

##import matplotlib.pyplot as plt

class Test_rungekuttaint(unittest.TestCase):
    ''' 
    Test script for the Runge Kutta integration function developed as the
    solution to the AOE 4404 Homework 6 Problem 3.
    
    @author: Matt Marti
    @date: 2019-06-28
    '''
    
    def test_nominal_4th_order(self):
        '''Test case 1: 4-th order Runge-Kutta'''
        
        def y(t):
            '''Truth value function'''
            f = np.zeros((2,t.shape[0]));
            f[0] = sp.exp(t);
            f[1] = sp.sin(t) + 5;
            return f;
        #
        
        def dy(t, y):
            '''Differential equation definition'''
            y = y.squeeze();
            if type(t) is not np.ndarray:
                f = np.zeros((2,1));
                f[0] = y[0];
                f[1] = sp.cos(t);
            else:
                f = np.zeros((2,t.shape[0]));
                f[0,:] = y[0,:];
                f[1,:] = sp.cos(t).squeeze();
            #
            return f;
        #
        
        # Function input
        ydot = lambda t, y : dy(t, y);
        y0 = np.ndarray((2,1));
        y0[0] = 1;
        y0[1] = 5;
        tlims = [0, 3];
        h = 0.001;
        
        # Truth values
        yfun = lambda t : y(t);
        
        # Compute test values
        [yout, tout, ydotout] = runge_kutta_int(ydot, y0, tlims, h);
        
        # Compute error
        thist = np.arange(tlims[0], tlims[1]+h, h);
        errhist = np.abs(yfun(thist) - yout);
        errdothist = np.abs(ydot(thist, yfun(thist)) - ydotout);
        maxerr = np.max(abs(errhist));
        maxerrdot = np.max(errdothist)
        
        ## Plot
        #plt.plot(errhist.T)
        #plt.plot(errdothist.T)
        #plt.show()
        
        # Assertions
        self.assertLess(np.max(np.abs(thist - tout)), 1e-12, 'Bad Runge Kutta Time History');
        self.assertLess(maxerrdot, 1e-12, 'Bad Output time derivative history');
        self.assertLess(maxerr, 1e-12, 'Bad Runge Kutta Solution History');
    #
    
    def test_nominal_3rd_order(self):
        '''Test case 2: 3-rd order Runge-Kutta'''
        
        def y(t):
            '''Truth value function'''
            f = np.zeros((2,t.shape[0]));
            f[0] = sp.exp(t);
            f[1] = sp.sin(t) + 5;
            return f;
        #
        
        def dy(t, y):
            '''Differential equation definition'''
            y = y.squeeze();
            if type(t) is not np.ndarray:
                f = np.zeros((2,1));
                f[0] = y[0];
                f[1] = sp.cos(t);
            else:
                f = np.zeros((2,t.shape[0]));
                f[0,:] = y[0,:];
                f[1,:] = sp.cos(t).squeeze();
            #
            return f;
        #
        
        # Function input
        ydot = lambda t, y : dy(t, y);
        y0 = np.ndarray((2,1));
        y0[0] = 1;
        y0[1] = 5;
        tlims = [0, 3];
        h = 0.001;
        
        # Truth values
        yfun = lambda t : y(t);
        
        # Compute test values
        [yout, tout, ydotout] = runge_kutta_int(ydot, y0, tlims, h, 3);
        
        # Compute error
        thist = np.arange(tlims[0], tlims[1]+h, h);
        errhist = np.abs(yfun(thist) - yout);
        errdothist = np.abs(ydot(thist, yfun(thist)) - ydotout);
        maxerr = np.max(abs(errhist));
        maxerrdot = np.max(errdothist)
        
        ## Plot
        #plt.plot(errhist.T)
        #plt.plot(errdothist.T)
        #plt.show()
        
        # Assertions
        self.assertLess(np.max(np.abs(thist - tout)), 1e-12, 'Bad Runge Kutta Time History');
        self.assertLess(maxerrdot, 1e-5, 'Bad Output time derivative history');
        self.assertLess(maxerr, 1e-5, 'Bad Runge Kutta Solution History');
    #
    
    def test_nominal_2nd_order(self):
        '''Test case 3: 2-nd order Runge-Kutta'''
        
        def y(t):
            '''Truth value function'''
            f = np.zeros((2,t.shape[0]));
            f[0] = sp.exp(t);
            f[1] = sp.sin(t) + 5;
            return f;
        #
        
        def dy(t, y):
            '''Differential equation definition'''
            y = y.squeeze();
            if type(t) is not np.ndarray:
                f = np.zeros((2,1));
                f[0] = y[0];
                f[1] = sp.cos(t);
            else:
                f = np.zeros((2,t.shape[0]));
                f[0,:] = y[0,:];
                f[1,:] = sp.cos(t).squeeze();
            #
            return f;
        #
        
        # Function input
        ydot = lambda t, y : dy(t, y);
        y0 = np.ndarray((2,1));
        y0[0] = 1;
        y0[1] = 5;
        tlims = [0, 3];
        h = 0.001;
        
        # Truth values
        yfun = lambda t : y(t);
        
        # Compute test values
        [yout, tout, ydotout] = runge_kutta_int(ydot, y0, tlims, h, 2);
        
        # Compute error
        thist = np.arange(tlims[0], tlims[1]+h, h);
        errhist = np.abs(yfun(thist) - yout);
        errdothist = np.abs(ydot(thist, yfun(thist)) - ydotout);
        maxerr = np.max(abs(errhist));
        maxerrdot = np.max(errdothist)
        
        ## Plot
        #plt.plot(errhist.T)
        #plt.plot(errdothist.T)
        #plt.show()
        
        # Assertions
        self.assertLess(np.max(np.abs(thist - tout)), 1e-12, 'Bad Runge Kutta Time History');
        self.assertLess(maxerrdot, 2e-5, 'Bad Output time derivative history');
        self.assertLess(maxerr, 2e-5, 'Bad Runge Kutta Solution History');
    #
    
    def test_nominal_1st_order(self):
        '''Test case 4: 1-st order Runge-Kutta'''
        
        def y(t):
            '''Truth value function'''
            f = np.zeros((2,t.shape[0]));
            f[0] = sp.exp(t);
            f[1] = sp.sin(t) + 5;
            return f;
        #
        
        def dy(t, y):
            '''Differential equation definition'''
            y = y.squeeze();
            if type(t) is not np.ndarray:
                f = np.zeros((2,1));
                f[0] = y[0];
                f[1] = sp.cos(t);
            else:
                f = np.zeros((2,t.shape[0]));
                f[0,:] = y[0,:];
                f[1,:] = sp.cos(t).squeeze();
            #
            return f;
        #
        
        # Function input
        ydot = lambda t, y : dy(t, y);
        y0 = np.ndarray((2,1));
        y0[0] = 1;
        y0[1] = 5;
        tlims = [0, 3];
        h = 0.001;
        
        # Truth values
        yfun = lambda t : y(t);
        
        # Compute test values
        [yout, tout, ydotout] = runge_kutta_int(ydot, y0, tlims, h, 1);
        
        # Compute error
        thist = np.arange(tlims[0], tlims[1]+h, h);
        errhist = np.abs(yfun(thist) - yout);
        errdothist = np.abs(ydot(thist, yfun(thist)) - ydotout);
        maxerr = np.max(abs(errhist));
        maxerrdot = np.max(errdothist)
        
        ## Plot
        #plt.plot(errhist.T)
        #plt.plot(errdothist.T)
        #plt.show()
        
        # Assertions
        self.assertLess(np.max(np.abs(thist - tout)), 1e-12, 'Bad Runge Kutta Time History');
        self.assertLess(maxerrdot, 5e-2, 'Bad Output time derivative history');
        self.assertLess(maxerr, 5e-2, 'Bad Runge Kutta Solution History');
    #
    
    def test_nominal_5th_order(self):
        '''Test case 6: 5-th order, 6 stage Runge-Kutta'''
        
        def y(t):
            '''Truth value function'''
            f = np.zeros((2,t.shape[0]));
            f[0] = sp.exp(t);
            f[1] = sp.sin(t) + 5;
            return f;
        #
        
        def dy(t, y):
            '''Differential equation definition'''
            y = y.squeeze();
            if type(t) is not np.ndarray:
                f = np.zeros((2,1));
                f[0] = y[0];
                f[1] = sp.cos(t);
            else:
                f = np.zeros((2,t.shape[0]));
                f[0,:] = y[0,:];
                f[1,:] = sp.cos(t).squeeze();
            #
            return f;
        #
        
        # Function input
        ydot = lambda t, y : dy(t, y);
        y0 = np.ndarray((2,1));
        y0[0] = 1;
        y0[1] = 5;
        tlims = [0, 3];
        h = 0.001;
        
        # Truth values
        yfun = lambda t : y(t);
        
        # Compute test values
        [yout, tout, ydotout] = runge_kutta_int(ydot, y0, tlims, h, 6);
        
        # Compute error
        thist = np.arange(tlims[0], tlims[1]+h, h);
        errhist = np.abs(yfun(thist) - yout);
        errdothist = np.abs(ydot(thist, yfun(thist)) - ydotout);
        maxerr = np.max(abs(errhist));
        maxerrdot = np.max(errdothist)
        
        ## Plot
        #plt.plot(errhist.T)
        #plt.plot(errdothist.T)
        #plt.show()
        
        # Assertions
        self.assertLess(np.max(np.abs(thist - tout)), 1e-12, 'Bad Runge Kutta Time History');
        self.assertLess(maxerrdot, 5e-14, 'Bad Output time derivative history');
        self.assertLess(maxerr, 5e-14, 'Bad Runge Kutta Solution History');
    #
#