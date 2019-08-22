#pragma once

#include <chrono>
#include <iostream>

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
@date: 2019-07-13
*/
class unittest {

public:

    // Constructor
    unittest(const char* msg = "");

    // Overload () operator to evaluate a test
    bool operator()(bool test_case);
    bool operator()(bool (&test_case)());
    bool operator()(bool(&test_case)(unittest*));

    // Display function
    static void display_stats(bool display_number_of_assertion_calls = false);

    // Reset timer and number of tests/instantiations/failed tests
    static void reset();

    // Assert that a statement is true. Print failure message 'msg' if failed.
    bool assert_true(bool a, const char* msg) {
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
    bool assert_false(bool a, const char* msg) {
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
    bool assert_equal(double a, double b, const char* msg) {
        return assert_equal(a, b, 1e-6, msg);
    }

    // Assert two floats are equal. Print failure message 'msg' if failed.
    bool assert_equal(float a, float b, const char* msg) {
        return assert_equal((double) a, (double) b, 1e-6, msg);
    }

    // Assert a float and a double are equal. Print failure message 'msg' if failed.
    bool assert_equal(float a, double b, const char* msg) {
        return assert_equal((double) a, b, 1e-6, msg);
    }

    // Assert a double and a float are equal. Print failure message 'msg' if failed.
    bool assert_equal(double a, float b, const char* msg) {
        return assert_equal(a, (double) b, 1e-6, msg);
    }

    // Assert two Ts are equal. Print failure message 'msg' if failed.
    template<typename A, typename B>
    bool assert_equal(A a, B b, const char* msg) {
        assertion_call();
        if (a != b) {
            test_fail();
            print_failure_intro();
            std::cout << "Expected " << a << " but was " << b << "." << std::endl;
            print_error_message(msg);
            return false;
        }
        return true;
    }

    // Assert two Ts are equal. Print failure message 'msg' if failed.
    bool assert_equal(double a, double b, double precision, const char* msg) {
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

    // Assert a is less than b
    template<typename A, typename B>
    bool assert_less(A a, B b, const char* msg) {
        assertion_call();
        if (a >= b) {
            test_fail();
            print_failure_intro();
            std::cout << "Argument " << a << " is more than " << b << "." << std::endl;
            print_error_message(msg);
            return false;
        }
        return true;
    }

    // Assert a is less than or equal to b
    template<typename A, typename B>
    bool assert_lesseq(A a, B b, const char* msg) {
        assertion_call();
        if (a > b) {
            test_fail();
            print_failure_intro();
            std::cout << "Argument " << a << " is more than " << b << "." << std::endl;
            print_error_message(msg);
            return false;
        }
        return true;
    }

    // Assert a is more than b
    template<typename A, typename B>
    bool assert_more(A a, B b, const char* msg) {
        assertion_call();
        if (a <= b) {
            test_fail();
            print_failure_intro();
            std::cout << "Argument " << a << " is less than " << b << "." << std::endl;
            print_error_message(msg);
            return false;
        }
        return true;
    }

    // Assert a is more than or equal to b
    template<typename A, typename B>
    bool assert_moreeq(A a, B b, const char* msg) {
        assertion_call();
        if (a < b) {
            test_fail();
            print_failure_intro();
            std::cout << "Argument " << a << " is larger than " << b << "." << std::endl;
            print_error_message(msg);
            return false;
        }
        return true;
    }

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
    static void print_exception_data();

    // Time handling variables/functions
    static std::chrono::high_resolution_clock::time_point t0; // Start time of tests
};