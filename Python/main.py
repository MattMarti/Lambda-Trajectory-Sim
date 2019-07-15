'''
main.py

Entry point to the Lambda Trajectory Sim program.

This program models the flight of a hybrid or liquid bi-prop rocket through
the atmosphere.

@dependencies
python 3.6.0

@author: Matt Marti
@date: 2019-06-05
'''

def main():
    from Simulation.sim_driver import run_sim
    
    # Run the simulation with precomputed design parameters. Eventually a GUI
    # will be used to select the parameters.
    run_sim();
#

# If this is the main function, do the main
if __name__ == '__main__':
    print("This is main");
    main();
#