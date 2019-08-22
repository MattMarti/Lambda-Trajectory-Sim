#pragma once

#include <vector>
#include "Eigen/Dense"

namespace Numerical_Methods {
    
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
    const Eigen::MatrixXd &yhist - M x N Matrix
                                   Function value time history, where N is 
                                   the length of the dataset and M is the 
                                   number different of rows to take the 
                                   derivative of. N corresponds to the 
                                   number of samples in the time history 
                                   of the dataset.
    const Eigen::VectorXd &thist - N legnth vector
                                   Vector of time values of each 
                                   measurement.
    unsigned int n               - (Optional) Order of finite difference. 
                                   Default is 1.
    
    @return
    ydothist                  - N length vector
                                Finite difference derivative time history
    
    @dependencies
    Eigen/Dense
    
    @author: Matt Marti
    @date: 2019-07-13
    */
    Eigen::MatrixXd finite_difference(const Eigen::MatrixXd &yhist, const Eigen::VectorXd &thist, unsigned int n = 1);
}