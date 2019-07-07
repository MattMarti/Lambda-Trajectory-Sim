#include "LTS/test_numerical_methods.h"
#include "LTS/Numerical_Methods.h"
#include "LTS/Test/Unittest.h"

#include "LTS/Numerical_Methods/test_finite_difference.h"

#include <iostream>

/*
Run all tests for the numerical methods.
*/
void Numerical_Methods::test_Numerical_Methods() {
    test_finite_difference_main();
}