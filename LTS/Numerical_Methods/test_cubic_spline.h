#pragma once

#include "LTS/Test/unittest.h"

namespace Numerical_Methods {

    namespace test_cubic_spline {
        /*
        Test Cubic Spline

        Test case for the cubic spline object

        @dependencies
        Eigen

        @author: Matt Marti
        @date: 2019-07-14
        */
        void test_main();

        bool test_nominal(unittest* test);
        bool test_clampbed_bc(unittest* test);
        bool test_out_of_range(unittest* test);
    }
}