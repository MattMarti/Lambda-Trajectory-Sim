#pragma once

#include "LTS/Test/unittest.h"

namespace Numerical_Methods {
    namespace test_finite_difference {
        /*
        Test_finite_difference main

        Test case for the finite difference function

        @dependencies
        python 3.6.0
        unittest
        numpy

        @author: Matt Marti
        @date: 2019-07-07
        */
        void test_main();

        bool test_nominal(unittest* test);
        bool test_multi(unittest* test);
        bool test_default_n_value(unittest* test);
        bool test_random_t_dist(unittest* test);
    }
}