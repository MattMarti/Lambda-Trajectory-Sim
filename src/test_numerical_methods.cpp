#include "test_numerical_methods.h"
#include "numerical_methods.h"
#include "Test/Unittest.h"

#include "Numerical_Methods/test_finite_difference.h"

#include <iostream>

/*
Run all tests for the numerical methods.
*/
void numerical_methods::test_numerical_methods() {
    test_finite_difference_main();
}