#ifndef LAMBDA_TRAJECTORY_SIM_SRC_UTIL_MATH_DIFFEQ_INTEGRATOR_HPP
#define LAMBDA_TRAJECTORY_SIM_SRC_UTIL_MATH_DIFFEQ_INTEGRATOR_HPP

#include <vector>

/**
Provides an interface for integrating Ordinary Differential Equations.
*/
class Integrator {

protected:
    double dt;

public:

    /// Iterates via one integration time step
    /// @param n Number of steps to integrate
    virtual void iterate(int n = 1) = 0;
};
#endif