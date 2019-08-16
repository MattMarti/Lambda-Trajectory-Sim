#ifndef ROCKET_COMPONENTS_ROCKET_COMPONENT_H
#define ROCKET_COMPONENTS_ROCKET_COMPONENT_H

#include <vector>

/*
Rocket_Component.h

This abstract class defines the base class for all rocket components.
Rocket components contain a list of child components. It also has mass
properties (mass, 3-axis moment of inertia)
*/
class Rocket_Component {

private:

    // The list of child components
    std::vector<Rocket_Component> components_vec;

public:

    /* ---------------- Properties ---------------- */

    // Mass
    double m;

    // Moment of Inertia about Axis 1
    double I1;

    // Moment of Inertia about Axis 2
    double I2;

    // Moment of Inertia about Axis 3
    double I3;

    /* ---------------- Functions ---------------- */

    void add_child(Rocket_Component c);
};

#endif