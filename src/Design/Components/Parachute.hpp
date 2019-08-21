#ifndef LAMBDA_TRAJECTORY_SIM_SRC_ROCKET_COMPONENTS_PARACHUTE_HPP
#define LAMBDA_TRAJECTORY_SIM_SRC_ROCKET_COMPONENTS_PARACHUTE_HPP

#include "Design/Components/Recovery_Device.hpp"

/*
Parachute.h

A parachute recovery device. Changes drag coefficient on deployment
*/
class Parachute : public Recovery_Device {
    Parachute();
};
#endif