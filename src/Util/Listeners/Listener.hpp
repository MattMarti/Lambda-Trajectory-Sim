#ifndef LAMBDA_TRAJECTORY_SIM_SRC_UTIL_LISTENERS_LISTENER_HPP
#define LAMBDA_TRAJECTORY_SIM_SRC_UTIL_LISTENERS_LISTENER_HPP

/// \brief Abstract class which listens for a particular event. For example, a listener can be set to check if the stage fuel is at or below zero mass.
class Listener {
    
public:

    /// \brief Returns true if the thing which the listener is looking for is true
    virtual bool event() = 0;
};

#endif