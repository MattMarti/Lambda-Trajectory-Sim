#include "Util/Math/DiffEq/Euler_Method.hpp"

Euler_Method::Euler_Method(double delta_t) {
    dt = delta_t;
}

/// Iterates via one integration time step
void Euler_Method::iterate(int n) {

    // get dx_dt = f(x_k)

    // x_kp1 = x_k + dt * dx_dt

}