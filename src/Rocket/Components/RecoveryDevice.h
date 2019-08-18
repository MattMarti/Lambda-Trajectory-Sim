#ifndef ROCKET_COMPONENTS_RECOVERY_DEVICE_H
#define ROCKET_COMPONENTS_RECOVERY_DEVICE_H

#include "Rocket/Components/InternalComponent.h"

/*
RecoveryDevice.h

Represents a recovery device, which can deploy at a specified alitude or time.
Once deployed, affects drag coefficient.
*/
class RecoveryDevice : public InternalComponent {
    RecoveryDevice();
};
#endif