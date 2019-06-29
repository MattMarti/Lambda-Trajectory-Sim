'''
Unit_Tests_Manual.py

Runs all unit tests in the Lambda Trajectory Sim.

This python script is meant to be a temporary driver for unit testing, until
I learn how to actually write unit tests for python.

@dependencies
python 3.6.0

@author: Matt Marti
@date: 2019-06-05
'''



def run_unit_tests():
    from Functions.Numerical_Methods.Test_cubicsplineInterp import Test_cubicsplineInterp
#

# If this is the main function, do the main
if __name__ == '__main__':
    run_unit_tests();
#