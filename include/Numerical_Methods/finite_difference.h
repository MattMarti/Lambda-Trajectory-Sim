#pragma once

#include <vector>

namespace numerical_methods {
    
    /*
    Forward, Central, Backwards finite difference calculation of derivative

    This function uses the Central Finite Difference method to compute the
    derivative for the given data vector.At the ends of the array, central
    difference doesn't work, so the forward difference method and backwards
    difference methods are used instead.

    Note that this function decides for you to use forward and bakwards
    differencing functions at either end of the dataset.This cannot be
    turned off or changed.

    @arg
    yhist - M x N numpy.ndarray
    Function value time history, where N is the length of the
    dataset and M is the number different things to take the
    derivative of.M is usually 1. N corresponds to the number
    of samples in the time history of the dataset.
    h - double
    Time step
    n - double(optional)
    Order of finite difference
    customge - bool(optional)
    Specify to use the custom gauss elimination function.
    True to use the function, False use numpy's built in function.
    False by default.

    @return
    ydothist - N x M numpy.ndarray
    Finite difference derivative time history

    @dependencies
    Eigen / Dense

    @author: Matt Marti
    @date: 2019 - 06 - 14
    */
    double finite_difference(std::vector<double> yhist, double h, unsigned int n = 1);
}