#ifndef ROCKET_COMPONENTS_ROCKET_COMPONENT_H
#define ROCKET_COMPONENTS_ROCKET_COMPONENT_H

#include <vector>

/*
Rocket_Component.h

This abstract class defines the base class for all rocket components.
Rocket components contain a list of child components. It also has mass
properties (mass, 3-axis moment of inertia)
*/
class RocketComponent {

private:

    // The list of child components
    std::vector<RocketComponent*> componentsptr_vec;

public:

    /* ---------------- Properties ---------------- */

    // Component Mass
    double component_m;

    // Component Moment of Inertia about Axis 1
    double component_I1;

    // Component Moment of Inertia about Axis 2
    double component_I2;

    // Component Moment of Inertia about Axis 3
    double component_I3;

    /* ---------------- Functions ---------------- */

    // Adds a component to the component list
    void add_child(RocketComponent* c);

    double get_m();
    double get_I1();
    double get_I2();
    double get_I3();

    // Destructor
    ~RocketComponent();
};
#endif