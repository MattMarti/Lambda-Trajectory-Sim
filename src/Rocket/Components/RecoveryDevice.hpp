#ifndef LAMBDA_TRAJECTORY_SIM_SRC_ROCKET_COMPONENTS_RECOVERY_DEVICE_HPP
#define LAMBDA_TRAJECTORY_SIM_SRC_ROCKET_COMPONENTS_RECOVERY_DEVICE_HPP

#include "Rocket/Components/InternalComponent.hpp"

/*
RecoveryDevice.h

Represents a recovery device, which can deploy at a specified alitude or time.
Once deployed, affects drag coefficient.
*/
class RecoveryDevice : public InternalComponent {
    RecoveryDevice();
};
#endif