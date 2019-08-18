#ifndef ROCKET_COMPONENTS_INTERNAL_COMPONENT_H
#define ROCKET_COMPONENTS_INTERNAL_COMPONENT_H

#include "Rocket/Components/StructuralComponent.h"
/*
Internal_Component.h

An internal component that affects the mass of the rocket, but not aerodynamics
*/
class InternalComponent : public StructuralComponent {
    InternalComponent();
};
#endif