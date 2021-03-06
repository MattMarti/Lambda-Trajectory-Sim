#include "Util/Software_in_the_loop_driver.hpp"
#include <vector>
#include <tuple>
#include <iostream>
#include <cmath>
#include <chrono>

#include "Util/Math/DiffEq/Differential.hpp"
#include "Util/Math/DiffEq/Euler_Method.hpp"

class Integration_Tester : public Differential {

public:

    double delta_t;

    std::vector<double> x = std::vector<double>(3);

    Integration_Tester(double dt) {
        delta_t = dt;
        x[0] = 0.0;
        x[1] = 0.0;
        x[2] = 10.0;
    }

    double & operator[](long ii) final {
        return x[ii];
    }

    inline std::vector<double> f() final {
        std::vector<double> dx_dt(3);
        dx_dt[0] = x[1] * delta_t + 0.5 * x[2] * delta_t * delta_t;
        dx_dt[1] = x[2] * delta_t;
        dx_dt[2] = 0.0;
        return dx_dt;
    }

    inline long size() final {
        return 3;
    }
};

void drive_sim() {
    using namespace std;

    // Parameters
    int JJ = 100;
    double delta_t = 0.01;
    double T = 10;
    int K = round(T / delta_t);
    double x0 = 0.0;
    double x1 = 0.0;
    double x2 = 10.0;
    int k = 0;

    // ODE object
    Integration_Tester x = Integration_Tester(delta_t);
    Euler_Method integrator = Euler_Method();

    // Loop integration for Run-Time-Polymorphism
    auto t0 = chrono::steady_clock::now();
    for (int jj = 0; jj < JJ; jj++) {

        // Parameters
        x0 = 0.0;
        x1 = 0.0;
        x2 = 10.0;

        // ODE object
        x[0] = 0.0;
        x[1] = 0.0;
        x[2] = 10.0;
        //inter = Euler_Method(delta_t);
        //Integrater<Integration_Tester> inter = Integrater<Integration_Tester>();

        // Integrate
        k = 0;
        while (k < K) {

            // Euler Integrate
            integrator.iterate(x);

            // Iterate
            k++;
        }
    }
    auto tF = chrono::steady_clock::now();
    cout << "\tk = " << k << ",\tx1 = " << x[0] << ",\tx2 = " << x[1] << ",\tx3 = " << x[2] << endl;
    cout << "Average elapsed time: " 
        << chrono::duration_cast<chrono::nanoseconds>(tF - t0).count() / JJ 
        << " Nanoseconds."
        << endl;

    return;
}
