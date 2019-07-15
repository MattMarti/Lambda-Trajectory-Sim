import unittest;
import numpy as np;
from gauss_elimination import gauss_elimination;

class Test_gauss_elimination(unittest.TestCase):
    '''
    Test_gauss_elimination
    
    Test case for the Gauss Elimination function, which solves linear systems.
    
    @dependencies
    python 3.6.0
    unittest
    numpy
    
    @author: Matt Marti
    @date: 2019-06-05
    '''

    # Test that the function works in a nominal case with numpy matrices
    def test_nominal_01(self):
    
        # Given
        A = np.array([[ 3,  2, -3,  1,  6], \
                      [ 6,  2,  4,  0,  5], \
                      [-3,  1,  0,  2,  3], \
                      [ 5, -8,  1,  2,  6], \
                      [ 5, -8,  1,  4,  6]],\
                     dtype=np.float64);
        B = np.array([[-24, 5 ],  \
                      [-6,  3 ],  \
                      [-9,  8 ],  \
                      [ 24, 2 ],  \
                      [ 36, 12]], \
                     dtype=np.float64 );
        #
        
        # True solution
        xtru = np.linalg.solve( A, B );
        
        # Computed solution
        [ x_soln, A_aug ] = gauss_elimination( A, B, True );
        
        # Check x solution
        precision = 1e-12;
        for i in range(0, xtru.shape[0] ):
            for j in range( 0, xtru.shape[1] ):
                assert abs(xtru[i,j] - x_soln[i,j]) < precision, 'Wrong solution';
            #
            # Check that the triangular matrix is returned correctly
            for j in range( 0, i ):
                assert not A_aug[i,j], 'Non-zero element in lower triangular area';
            #
        #
    #
    
    # A matrix that actually needs partial pivoting, and no use of numpy matrices
    def test_nominal_02(self):
        
        # Given
        A = np.array([[1, 1, 1], [2, 2, 1], [3, 4, 2]]);
        B = np.array([[1], [2], [2]]);
        
        # True solution
        xtru = np.linalg.solve( A, B );
        
        # Computed solution
        [ x_soln, A_aug ] = gauss_elimination( A, B, True );
        
        # Check x solution
        precision = 1e-12;
        for i in range( 0, xtru.shape[0] ):
            for j in range( 0, xtru.shape[1] ):
                assert abs(xtru[i,j] - x_soln[i,j]) < precision, 'Wrong solution';
            #
            # Check that the triangular matrix is returned correctly
            for j in range( 0, i ):
                assert not A_aug[i,j], 'Non-zero element in lower triangular area';
            #
        #
    #
    
    # 
    def test_single_values(self):
        
        # Test with ints
        a = np.ndarray((1,1));
        a[0,0] = 2;
        b = np.ndarray((1,1));
        b[0,0] = 10;
        x = gauss_elimination(a,b);
        self.assertAlmostEqual(x[0,0], 5, 'Failed for scalar values');
        
        # Test with float result
        a[0,0] = 2;
        b[0,0] = 3;
        x = gauss_elimination(a,b);
        self.assertAlmostEqual(x[0,0], 1.5, 'Failed for scalar values');
    #
    
    # Only works with numpy.ndarrays
    def test_types(self):
        
        # Valid inputs from test_02
        A = np.array([[1, 1, 1], [2, 2, 1], [3, 4, 2]]);
        B = np.array([[1], [2], [2]]);
        
        # Give the function a bad type
        x = 'Five'; # String type
        y = False; # Bool type
        z = [5, 5, 1]; # List type
        w = [[1], [2], [2]]; # List type
        
        # Assertions
        self.assertRaises(TypeError, gauss_elimination, A, x);
        self.assertRaises(TypeError, gauss_elimination, A, y);
        self.assertRaises(TypeError, gauss_elimination, A, z);
        self.assertRaises(TypeError, gauss_elimination, A, w);
        self.assertRaises(TypeError, gauss_elimination, x, B);
        self.assertRaises(TypeError, gauss_elimination, y, B);
        self.assertRaises(TypeError, gauss_elimination, z, B);
        self.assertRaises(TypeError, gauss_elimination, w, B);
    #
#

