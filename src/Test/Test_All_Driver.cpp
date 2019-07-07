#include <iostream>

#include "Test/unittest.h"
#include "Test/Test_All_Driver.h"
#include "test_numerical_methods.h"

int test_all() {

	// Run Tests
    numerical_methods::test_numerical_methods();

	// Output
	unittest::display_stats(true);

	return 0;
}