#include "Eigen/Dense"

from secant_root_solve import secant_root_solve;

class Test_secant_root_solve(unittest.TestCase):
    '''
    Test_secantrootsolve.m
    
    Test case for the Secant Root Solver function. Based on the solution to
    Problem 2 of Homework 1 f AOE 4404 Numerical Methods
    
    Use Graphical technique, bisection method, false-position, fixed-point
    iteration, Netwon method, and secant method to find the first root of
        f(x) = x*exp(x) - cos(x)
    
    @author: Matt Marti
    @date: 2019-06-16
    '''
    
    def test_only(self):
        '''Only test needed'''
        
        # Define function
        f = lambda x : math.cos(x) - x*math.exp(x);
        
        # Parameters
        a = 0; # Lower bound
        b = 1; # Upper bound
        errstop = 1e-12; # Stopping criteria
        maxiter = 1000;
        
        # Function call
        x, niter, erra = secant_root_solve(f, a, b, maxiter, errstop);
        
        # Check results
        self.assertLess(abs(f(x)), errstop, \
            'Results error not less than specified error');
        self.assertLess(abs(erra), errstop, \
            'Results error not less than specified error');
        self.assertLess(niter, maxiter, \
            'Took too many iterations, function could be bugged');
        #
    #
#