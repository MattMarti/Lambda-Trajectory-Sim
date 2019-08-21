#ifndef LAMBDA_TRAJECTORY_SIM_SRC_ROCKET_COMPONENTS_INTERNAL_COMPONENT_HPP
#define LAMBDA_TRAJECTORY_SIM_SRC_ROCKET_COMPONENTS_INTERNAL_COMPONENT_HPP

#include "Rocket/Components/StructuralComponent.hpp"
/*
Internal_Component.h

An internal component that affects the mass of the rocket, but not aerodynamics
*/
class InternalComponent : public StructuralComponent {
    InternalComponent();
};
#endif