#pragma once

#include "test/unittest.h"

namespace numerical_methods {
    
    /*
    Test_finite_difference main

    Test case for the finite difference function

    @dependencies
    python 3.6.0
    unittest
    numpy

    @author: Matt Marti
    @date: 2019 - 06 - 14
    */
    void test_finite_difference_main();
    
    bool test_nominal_01(unittest* test);
    bool test_nominal_02(unittest* t);
    bool test_default_n_value(unittest* t);
    bool test_customge(unittest* t);
}