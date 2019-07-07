#pragma once

#include <vector>
#include "Eigen/Dense"

namespace numerical_methods {
    
    /*
    Forward, Central, Backwards finite difference calculation of derivative
    This function uses the Central Finite Difference method to compute the
    derivative for the given data vector. At the ends of the array, central
    difference doesn't work, so the forward difference method and backwards
    difference methods are used instead.
    
    Note that this function decides for you to use forward and bakwards
    differencing functions at either end of the dataset. This is to avoid
    the problem of running out of data on either side of a particular data
    point.
    
    @arg
    std::vector<double> yhist - N length vector
                                Function value time history, where N is the length of the
                                dataset and M is the number different things to take the
                                derivative of. M is usually 1. N corresponds to the number
                                of samples in the time history of the dataset.
    double h                  - Time step
    unsigned int n            - (Optional) Order of finite difference. Default is 1.
    
    @return
    ydothist                  - N length vector
                                Finite difference derivative time history
    
    @dependencies
    Eigen/Dense
    
    @author: Matt Marti
    @date: 2019-07-06
    */
    double finite_difference(std::vector<double> yhist, double h, unsigned int n = 1);
}