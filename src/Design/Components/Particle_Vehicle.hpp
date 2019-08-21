#ifndef LAMBDA_TRAJECTORY_SIM_SRC_DESIGN_COMPONENTS_PARTICLE_VEHICLE_HPP
#define LAMBDA_TRAJECTORY_SIM_SRC_DESIGN_COMPONENTS_PARTICLE_VEHICLE_HPP

#include <vector>
#include "Design/Components/Vehicle.hpp"

/**
A simple particle. The only component it contains is itself.
*/
class Particle_Vehicle : public Vehicle {

public:

    double get_m();
    std::vector<double> get_I();
    std::vector<double> sum_forces();
    std::vector<double> get_pos();
    std::vector<double> get_vel();
    std::vector<double> get_acc();
    std::vector<double> get_quat();
    std::vector<double> get_omega();
};
#endif