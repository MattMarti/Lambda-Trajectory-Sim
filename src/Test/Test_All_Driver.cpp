#include <iostream>

#include "LTS/Test/unittest.h"
#include "LTS/Test/Test_All_Driver.h"
#include "LTS/test_Numerical_Methods.h"

int test_all() {

    // Run Tests
    Numerical_Methods::test_Numerical_Methods();

    // Output
    unittest::display_stats(true);

    return 0;
}