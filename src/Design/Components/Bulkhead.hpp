#ifndef LAMBDA_TRAJECTORY_SIM_SRC_ROCKET_COMPONENTS_BULKHEAD_HPP
#define LAMBDA_TRAJECTORY_SIM_SRC_ROCKET_COMPONENTS_BULKHEAD_HPP

#include "Design/Components/Radius_Ring_Component.hpp"

/*
Bulkhead.h

A solid bulkhead (inner radius zero)
*/
class Bulkhead : public Radius_Ring_Component {
    Bulkhead();
};
#endif