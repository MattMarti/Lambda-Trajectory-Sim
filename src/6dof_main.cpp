#include <iostream>

#include "Design/Components/Component.hpp"
#include "Util/Sim_Driver.hpp"

// Entry point to 6dof simulation. Prases input argument and drives sim
int main(int argc, char **argv) {
    using namespace std;

    // Parse input arguments
    if (argc == 0) {
        cout << "Print Help Menu" << endl;
        cout << "USAGE:" << endl;
        cout << "-ork [FILE]  : \".ork\" file which contains the model of the rocket" << endl;
        cout << "-tc [FILE]   : \".csv\" file which contains the thrust curve of the motor" << endl;
        cout << "-env [FILE]  : \".csv\" file which contains the [lat lon alt]" << endl;
        cout << "-wind [FILE] : \".csv\" file which contains precomputed wind speed values" << endl;
    }
    for (int i = 0; i < argc; i++) {
        cout << argv[i] << endl;
    }


    // Load open rocket from example

    // Run Simulation
    drive_sim();

    // Save data

    return 0;
}