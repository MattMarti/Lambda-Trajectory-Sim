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
    Euler_Method();

    /// Iterates via one integration time step
    /// @param obj Differential object to integrate
    /// @param n Number of steps to integrate
    void iterate(Differential& obj, int n = 1) override {
        long ii, jj;
        for (ii = 0; ii < n; ii++) {
            auto dx_dt = obj.f();
            for (jj = 0; jj < obj.size(); jj++) {
                obj[jj] = obj[jj] + dx_dt[jj];
            }
        }
    }
};
#endif