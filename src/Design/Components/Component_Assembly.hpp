#ifndef LAMBDA_TRAJECTORY_SIM_SRC_ROCKET_COMPONENTS_COMPONENT_ASSEMBLY_HPP
#define LAMBDA_TRAJECTORY_SIM_SRC_ROCKET_COMPONENTS_COMPONENT_ASSEMBLY_HPP

#include "Design/Components/Component.hpp"

/*
Component_Assembly.h

Base component for an assembly of external components. Can be extended to allow
multiple rocket bodies next to each other.
*/
class Component_Assembly : public Component {

    Component_Assembly();
};
#endif
