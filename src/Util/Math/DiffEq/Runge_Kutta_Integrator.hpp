#ifndef LAMBDA_TRAJECTORY_SIM_SRC_UTIL_MATH_DIFFEQ_RUNGE_KUTTA_INTEGRATOR_HPP
#define LAMBDA_TRAJECTORY_SIM_SRC_UTIL_MATH_DIFFEQ_RUNGE_KUTTA_INTEGRATOR_HPP

#include "Util/Math/DiffEq/Integrator.hpp"

/**
Runge-Kutta Integration class. Integrates an Ordinary Differential Equation
with optional polynomial interpolation for increased accuracy.
*/
class Runge_Kutta_Integrator : public Integrator {

public:

    void iterate();
    

};
#endif