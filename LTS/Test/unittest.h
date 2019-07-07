#pragma once

#include <chrono>
#include <string>

/*
Unit Test Class

Provides utilities for running unit tests in C++. This class employs private 
static variables to measure the number of tests ran, the number of tests 
failed, the time it took to run the tests, etc. It also provides a utitlity
to display this data to the command window.

Test cases may be passed as pointers to functions using the () operator. The
() operator provides a method to pass this object as an argument so that test
cases can use the utilities provided without instantiating a new unittest 
object.

@author: Matt Marti
@date: 2019-07-06
*/
class unittest {

public:

    // Constructor
    unittest();

    // Overload () operator to evaluate a test
    bool operator()(bool test_case);
    bool operator()(bool (*fncptr)());
    bool operator()(bool(*fncptr)(unittest* testobj));

    // Display function
    static void display_stats(bool display_number_of_assertion_calls = false);

    // Reset timer and number of tests/instantiations/failed tests
    static void reset();

    // Assertion functions
    static bool assert_true(bool a, const char* msg = "");
    static bool assert_false(bool a, const char* msg = "");
    static bool assert_equal(double a, double b, const char* msg = "");
    static bool assert_equal(double a, double b, double precision = 1.0e-6, const char* msg = "");

private:

    // Test stats
    static unsigned long num_tests;
    static unsigned long num_tests_failed;
    static unsigned long num_exceptions;
    static unsigned long num_instantiations;
    static unsigned long num_assertions;
    static unsigned long num_assertions_failed;

    // Incrementors
    static void test_fail(); // Increments the number of failed tests
    static void assertion_call(); // Increments the assertion counter

    // Assertion stuff
    static void print_failure_intro();
    static void print_error_message(const char* msg);

    // Time handling variables/functions
    static std::chrono::high_resolution_clock::time_point t0; // Start time of tests
};