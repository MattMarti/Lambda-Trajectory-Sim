#ifndef LAMBDA_TRAJECTORY_SIM_SRC_ROCKET_COMPONENTS_BULKHEAD_HPP
#define LAMBDA_TRAJECTORY_SIM_SRC_ROCKET_COMPONENTS_BULKHEAD_HPP

#include "Rocket/Components/RadiusRingComponent.hpp"

/*
Bulkhead.h

A solid bulkhead (inner radius zero)
*/
class Bulkhead : public RadiusRingComponent {
    Bulkhead();
};
#endif