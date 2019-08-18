#ifndef ROCKET_COMPONENTS_COMPONENT_ASSEMBLY_H
#define ROCKET_COMPONENTS_COMPONENT_ASSEMBLY_H

#include "Rocket/Components/RocketComponent.h"

/*
Component_Assembly.h

Base component for an assembly of external components. Can be extended to allow
multiple rocket bodies next to each other.
*/
class ComponentAssembly : public RocketComponent {

    ComponentAssembly();
};
#endif
