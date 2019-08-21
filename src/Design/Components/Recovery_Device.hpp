#ifndef LAMBDA_TRAJECTORY_SIM_SRC_ROCKET_COMPONENTS_RECOVERY_DEVICE_HPP
#define LAMBDA_TRAJECTORY_SIM_SRC_ROCKET_COMPONENTS_RECOVERY_DEVICE_HPP

#include "Design/Components/Internal_Component.hpp"

/*
Recovery_Device.h

Represents a recovery device, which can deploy at a specified alitude or time.
Once deployed, affects drag coefficient.
*/
class Recovery_Device : public Internal_Component {
    Recovery_Device();
};
#endif