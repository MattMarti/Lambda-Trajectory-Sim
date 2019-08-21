#ifndef LAMBDA_TRAJECTORY_SIM_SRC_ROCKET_COMPONENTS_ROCKET_COMPONENT_HPP
#define LAMBDA_TRAJECTORY_SIM_SRC_ROCKET_COMPONENTS_ROCKET_COMPONENT_HPP

#include <vector>
#include <string>

/*
Rocket_Component.h

This abstract class defines the base class for all rocket components.
Rocket components contain a list of child components. It also has mass
properties (mass, 3-axis moment of inertia)
*/
class RocketComponent {

public:
    RocketComponent();

    /* ---------------- Virtual Functions ---------------- */

    // Mass Functions
    double get_m();
    void set_m();
    bool is_override_m();

    // Moment of Inertia Functions
    std::vector<double> get_I();
    void set_I(std::vector<double> I_in);
    void set_Ix(double I_in);
    void set_Iy(double I_in);
    void set_Iz(double I_in);
    bool is_override_I();

    // Position Methods
    std::vector<double> get_cg();
    bool is_override_cg();

    /* ---------------- Common Functions ---------------- */

    // Adds a component to the component list
    void add_child(RocketComponent* c);

    // Name and program ID
    std::string get_name();
    int get_ID();

    // Destructor
    ~RocketComponent();

protected:

    // The list of child components
    std::vector<RocketComponent*> child_components;

    // Parent of this component
    RocketComponent * parent;

    // Name string
    std::string name;

    // ID
    int id;
};
#endif