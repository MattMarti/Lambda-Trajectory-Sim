#ifndef ROCKET_COMPONENTS_PARACHUTE_H
#define ROCKET_COMPONENTS_PARACHUTE_H

#include "Rocket/Components/RecoveryDevice.h"

/*
Parachute.h

A parachute recovery device. Changes drag coefficient on deployment
*/
class Parachute : public RecoveryDevice {
    Parachute();
};
#endif