#ifndef LAMBDA_TRAJECTORY_SIM_SRC_UTIL_MATH_DIFFEQ_EULER_METHOD_HPP
#define LAMBDA_TRAJECTORY_SIM_SRC_UTIL_MATH_DIFFEQ_EULER_METHOD_HPP

#include "Util/Math/DiffEq/Integrator.hpp"

/**
Simple Euler method for integrating ODEs.
*/
class Euler_Method : public Integrator {
public:

    /// Constructor
    /// @param delta_t Time step length between integration periods.
    Euler_Method(double delta_t);

    /// Iterates via one integration time step
    void iterate(int n = 1) override;
};
#endif