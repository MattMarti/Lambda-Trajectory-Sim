#include <vector>
#include "LTS/Numerical_Methods/test_finite_difference.h"
#include "LTS/Test/unittest.h"

/*
Test_finite_difference

Test case for the finite difference function

@dependencies
Eigen/Dense

@author: Matt Marti
@date: 2019-07-06
*/
void Numerical_Methods::test_finite_difference_main() {

    // Create Unit Test object
    unittest t = unittest("finite_difference");

    // Run tests
    t(&test_nominal_01);
    t(&test_nominal_02);
    t(&test_default_n_value);
    t(&test_customge);
}

    // Make sure all the orders work
bool Numerical_Methods::test_nominal_01(unittest* test) {
    using namespace std;
    
    return test->assert_equal(1, 0, "Test");
    /*
    // Function input
    h = 0.1;
    trange = np.arange(0, 10+h, h);
    thist = np.zeros((1,trange.shape[0])); // t = (0:h:10)'
    for i in range(0, trange.shape[0]):
        thist[0,i] = trange[i];
    //
    yhist = (-9.81/2)*thist**2 + 50*thist + 200;

    // Truth value
    ydottruthhist = -9.81*thist + 50;

    // Test Function call
    errvec = [5e-1, 1e-11, 1e-11, 1e-11, 1e-11, 1e-11, 2e-11, 3e-11, 5e-11];
    for n in range(1, 10):

        // Function call
        [ydothist] = finite_difference(yhist, h, n);

        // Compute maximum absolute error
        errhist = ydothist - ydottruthhist;
        maxerr = np.max(np.abs(errhist));
        self.assertLess(maxerr, errvec[n-1], \
            "Error for " + str(n) + " order polynomial is too high")
            //
        //
    //

    return false;*/
}

// Derivative of nonlinear function is approximate and all orders work.
// Also test that multiple data entries work.
bool Numerical_Methods::test_nominal_02(unittest* test) {
    return test->assert_equal(1, 0, "Test");
    /*
    // Create time array
    h = .1;
    t = np.arange(0, 10+h, h); // t = (0:h:10)'
    thist = np.zeros((1, t.shape[0]));
    for i in range(0, t.shape[0]):
            thist[0,i] = t[i];
    //

    // Create function values to differentiate
    sinvec = np.sin(thist);
    cosvec = np.cos(thist);
    yhist = np.zeros((2, t.shape[0]));
            yhist[0,:] = sinvec.copy();
            yhist[1,:] = cosvec.copy();

            // Truth value
            ydottruthhist = np.zeros((2, t.shape[0]));
            ydottruthhist[0,:] = cosvec.copy();
            ydottruthhist[1,:] = - sinvec.copy();

            // Test Function call
            errvec = [5e-1, 5e-3, 2.5e-4, 2.5e-5, 2e-6, 2e-7, 2e-8, 2e-9, 2e-10];
            for n in range(1, 10):

                // Function call
                ydothist = finite_difference(yhist, h, n);

                // Compute maximum absolute error
                errhist = ydothist - ydottruthhist;
                maxerr = np.max(np.abs(errhist));
                self.assertLess(maxerr, errvec[n-1], \
                    "Error for " + str(n) + " order polynomial is too high")
                //
            //
        //
    return false;*/
}

// Ensure that n is chosen by default if not specified
bool Numerical_Methods::test_default_n_value(unittest* test) {
    
    throw std::exception();

    return test->assert_equal(1, 0, "Test");
    /*
    // Function input
    h = 0.1;
    trange = np.arange(0, 10+h, h);
    thist = np.zeros((1,trange.shape[0])); // t = (0:h:10)'
    for i in range(0, trange.shape[0]):
        thist[0,i] = trange[i];
    //
    yhist = (-9.81/2)*thist**2 + 50*thist + 200;

    // Truth value
    ydottruthhist = -9.81*thist + 50;

    // Test Function call
    [ydothist] = finite_difference(yhist, h);

    // Compute maximum absolute error
    errhist = ydothist - ydottruthhist;
    maxerr = np.max(np.abs(errhist));

    // Assert max absolute error is within bounds
    self.assertLess(maxerr, 5e-1, \
        "Error for default order polynomial is too high")
    self.assertGreater(maxerr, 1e-1, \
        "Error for default order polynomial is too low")
    //
    return false;*/
}

// Ensure that if specified, the custom gauss_elimination function is used
bool Numerical_Methods::test_customge(unittest* test) {
    return test->assert_equal(1, 0, "Test");
    /*
    // Function input
    h = 0.1;
    trange = np.arange(0, 10+h, h);
    thist = np.zeros((1,trange.shape[0])); // t = (0:h:10)'
    for i in range(0, trange.shape[0]):
        thist[0,i] = trange[i];
    //
    yhist = (-9.81/2)*trange**2 + 50*trange + 200;

    // Truth value
    ydottruthhist = -9.81*thist + 50;

    // Test Function call
    [ydothist] = finite_difference(yhist, h, 1, True);

    // Compute maximum absolute error
    errhist = ydothist - ydottruthhist;
    maxerr = np.max(np.abs(errhist));

    // Assert max absolute error is within bounds
    self.assertLess(maxerr, 5e-1, \
        "Error for default order polynomial is too high")
    self.assertGreater(maxerr, 1e-1, \
        "Error for default order polynomial is too low")
    //
    //
    return false;*/
}