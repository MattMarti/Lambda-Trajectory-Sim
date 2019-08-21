#ifndef LAMBDA_TRAJECTORY_SIM_SRC_ROCKET_COMPONENTS_JOINT_COMPONENT_HPP
#define LAMBDA_TRAJECTORY_SIM_SRC_ROCKET_COMPONENTS_JOINT_COMPONENT_HPP

#include "Rocket/Components/StructuralComponent.hpp"

/*
JointComponent.h

This class defines a joint between two structural components. Used for 
structural analysis. Material properties listed here.
*/
class JointComponent : public StructuralComponent {
    JointComponent();
};
#endif