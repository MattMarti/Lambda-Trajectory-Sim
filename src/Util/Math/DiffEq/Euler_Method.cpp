#include "Util/Math/DiffEq/Euler_Method.hpp"

Euler_Method::Euler_Method() {}

/// Iterates via one integration time step
void iterate(Differential& obj, int n = 1) {
    long ii, jj;
    for (ii = 0; ii < n; ii++) {
        auto dx_dt = obj.f();
        for (jj = 0; jj < obj.size(); jj++) {
            obj[jj] = obj[jj] + dx_dt[jj];
        }
    }

}