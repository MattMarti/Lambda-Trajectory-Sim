#include <iostream>
#include <chrono>
#include "Test/unittest.h"

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
unittest::unittest() {num_instantiations++;}

// Overload () operator to evaluate a test. Argument is a boolean.
bool unittest::operator()(bool test_case) {
    num_tests++;
    if (!test_case) num_tests_failed++;
    return test_case;
}

// Overload () operator to evaluate a test. Argument is pointer to a function.
bool unittest::operator()(bool (*fncptr)()) {
    num_tests++;
    bool test_pass = false;
    try {
        test_pass = (*fncptr)();
        if (!test_pass) num_tests_failed++;
    }
    catch (...) {
        num_exceptions++;
    }
    return test_pass;
}

// Overload () operator to evaluate a test. Argument is pointer to a function.
bool unittest::operator()(bool (*fncptr)(unittest*)) {
    num_tests++;
    bool test_pass = false;
    try {
        test_pass = (*fncptr)(this);
        if (!test_pass) num_tests_failed++;
    }
    catch (...) {
        num_exceptions++;
    }
    return test_pass;
}

// Assert that a statement is true. Print failure message 'msg' if failed.
bool unittest::assert_true(bool a, const char* msg) {
    assertion_call();
    if (!a) {
        test_fail();
        print_failure_intro();
        std::cout << "Expected true but was false." << std::endl;
        print_error_message(msg);
        return false;
    }
    return true;
}

// Assert that a statement is false. Print failure message 'msg' if failed.
bool unittest::assert_false(bool a, const char* msg) {
    assertion_call();
    if (a) {
        test_fail();
        print_failure_intro();
        std::cout << "Expected false but was true." << std::endl;
        print_error_message(msg);
        return false;
    }
    return true;
}

// Assert two doubles are equal. Print failure message 'msg' if failed.
bool unittest::assert_equal(double a, double b, const char* msg) {
    return assert_equal(a, b, 1e-6, msg);
}

// Assert two doubles are equal. Print failure message 'msg' if failed.
bool unittest::assert_equal(double a, double b, double precision, const char* msg) {
    assertion_call();
    if (std::abs(a - b) > precision) {
        test_fail();
        print_failure_intro();
        std::cout << "Expected " << a << " but was " << b << "." << std::endl;
        print_error_message(msg);
        return false;
    }
    return true;
}

//Prints to the command line the statistics of the tests
void unittest::display_stats(bool display_number_of_assertion_calls) {
    using namespace std;
    using namespace std::chrono;

    // End Timer and Compute delta time
    high_resolution_clock::time_point tf = high_resolution_clock::now();
    auto delta_time = duration_cast<milliseconds>(tf - t0).count();

    // Print number of tests, failures, exceptions
    cout << endl;
    cout << " " << num_tests << " Test";
    if (num_tests != 1) cout << "s";
    cout << " ran, " << num_tests_failed << " failure";
    if (num_tests_failed != 1) cout << "s";
    cout << ", " << num_exceptions << " exception";
    if (num_exceptions != 1) cout << "s";
    cout << " were thrown." << endl;

    // Print Number of assertion calls
    if (display_number_of_assertion_calls) {
        cout << " " << num_assertions << " assertion call";
        if (num_assertions != 1) cout << "s";
        cout << ", " << num_assertions_failed << " failed assertion";
        if (num_assertions_failed != 1) cout << "s";
        cout << endl;
    }

    // Print time
    cout << " Total time: " << delta_time << " milliseconds" << endl;
    cout << endl;
}

// Reset timer and counters
void unittest::reset() {

    // Reset stats
    num_tests = 0;
    num_tests_failed = 0;
    num_exceptions = 0;
    num_instantiations = 0;
    num_assertions = 0;
    num_assertions_failed = 0;

    // Reset timer
    t0 = std::chrono::high_resolution_clock::now();
}

/* --------------------------- Private Parts --------------------------- */

// Private Assertion Incrementors
void unittest::assertion_call() {num_assertions++;}
void unittest::test_fail() {num_assertions_failed++;}

// Print messages
void unittest::print_failure_intro() {
    std::cout << " Assertion Failed: ";
}
void unittest::print_error_message(const char* msg) {
    std::cout << " --> " << msg << std::endl;
}

// Initialize Unit Test static variables
unsigned long unittest::num_tests = 0;
unsigned long unittest::num_tests_failed = 0;
unsigned long unittest::num_exceptions = 0;
unsigned long unittest::num_instantiations = 0;
unsigned long unittest::num_assertions = 0;
unsigned long unittest::num_assertions_failed = 0;

// Start time of tests. Initialized at run time. Private Variable. Ugly. Don't touch.
std::chrono::high_resolution_clock::time_point unittest::t0 \
    = std::chrono::high_resolution_clock::now();