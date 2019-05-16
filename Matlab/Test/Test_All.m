%% Test_All.m
% 
% Runs all unit tests in the Hybrid Rocket Flight Sim suite.
% 
% @author: Matt Marti
% @date: 2019-05-07

clear, clc, clear global

% Numerical Methods
Test_mmatth3_secantrootsolve_fun
Test_mmatth3_gausselimination_nonrow_fun
Test_mmatth3_cubicspline_fun
Test_mmatth3_rungekuttaint_fun
Test_mmatth3_finitedifference_fun

% Ambient
Test_stdAtmosphereCalc_hgp

% Dynamics
Test_dragCalc

% RocketEngine
Test_hybridRocketThrustCalc

% Time-dependent PDE for computing position
Test_fHRFSdynamics_1D







