#ifndef LAMBDA_TRAJECTORY_SIM_SRC_ROCKET_COMPONENTS_PARACHUTE_HPP
#define LAMBDA_TRAJECTORY_SIM_SRC_ROCKET_COMPONENTS_PARACHUTE_HPP

#include "Rocket/Components/RecoveryDevice.hpp"

/*
Parachute.h

A parachute recovery device. Changes drag coefficient on deployment
*/
class Parachute : public RecoveryDevice {
    Parachute();
};
#endif