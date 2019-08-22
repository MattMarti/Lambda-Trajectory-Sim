#ifndef LAMBDA_TRAJECTORY_SIM_SRC_UTIL_MATH_DIFFEQ_INTEGRATOR_HPP
#define LAMBDA_TRAJECTORY_SIM_SRC_UTIL_MATH_DIFFEQ_INTEGRATOR_HPP

#include <vector>
#include "Util/Math/DiffEq/Differential.hpp"

/**
Provides an interface for integrating Ordinary Differential Equations.
*/
class Integrator {

public:

    /// Iterates via one integration time step
    /// @param obj Differential object to integrate
    /// @param n Number of steps to integrate
    virtual void iterate(Differential& obj, int n = 1) = 0;
};
#endif