#ifndef LAMBDA_TRAJECTORY_SIM_SRC_UTIL_MATH_DIFFEQ_INTEGRATABLE_HPP
#define LAMBDA_TRAJECTORY_SIM_SRC_UTIL_MATH_DIFFEQ_INTEGRATABLE_HPP

#include <vector>

/**
Interface for Runge Kutta Integrator <code>Runge_Kutta_Integrator.hpp<\code>
function
*/
class Differential {

public:

    /// Returns the differential equation dx_dt = f(x)
    virtual std::vector<double> f() = 0;

    /// Returns number of elements in object state
    virtual long size() = 0;

    /// Allows access to elements of the object's state
    virtual double & operator[](long ii) = 0;
};
#endif