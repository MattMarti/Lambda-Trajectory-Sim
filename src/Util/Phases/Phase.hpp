#ifndef LAMBDA_TRAJECTORY_SIM_UTIL_PHASES_PHASE_HPP
#define LAMBDA_TRAJECTORY_SIM_UTIL_PHASES_PHASE_HPP

#include <vector>
#include "Lambda-Trajectory-Sim/src/Util/Listeners/Listener.hpp"

/*!
    \file
    \brief Defines a Phase abstract class,
           Provides an interface for phases of the simulation

*/

class Phase {

    /// \brief Contains simulation listeners for phase end conditions
    std::vector<Listener*> listeners;

public:

    /// \brief Returns true if the phase end conditions are met
    virtual bool is_over() = 0;

    /// \brief Add listeners to the phase
    void add_listener();

};

#endif