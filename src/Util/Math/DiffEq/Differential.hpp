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

    /// Grants access to object's current state
    virtual std::vector<double> get_state() = 0;

    /// Allows integrator to set the state
    virtual void set_state(std::vector<double> s) = 0;



};
#endif