%% One_D_INS_Example
%
% This script contains an exmaple of the principles of Inertial Navigation
% System. Random Truth data is generated for Position, Velocity, Accel.
% Then a Kalman Filter is used to estimate the error state with GPS
% measurements.
% 
% The idea behind an INS is to use a Kalman Filter to estimate the error
% state, and report the IMU estimated state minus the error. The IMU error
% could be driven to zero with a control loop, but this is not necessary
% for tracking over short periods of time. For example, in a model rocket
% flight to apogee.
% 
% @author: Matt Marti
% @date: 2019-08-26

clear, clc


%% Parameters

% Time
T = 10;
dt_imu = 0.01;
K_imu = round( T / dt_imu );
dt_gps = 0.05;
K_gps = round( T / dt_gps );

% Power spectral density of accelerometer
q_ins = 0.5;

% INS State transition
nx_ins = 3; % State Vector size
nv_ins = 3;
Fk_ins = [...
    1,  dt_imu,  dt_imu^2/2 ;
    0,  1,   dt_imu     ;
    0,  0,   1      ];

% IMU State transition
nx_ins = 3; % State Vector size
nv_ins = 3;
Fk_imu = [...
    1,  dt_imu,  dt_imu^2/2 ;
    0,  1,   dt_imu     ;
    0,  0,   1      ];

% Movement process noise
qC = 30; % Position Spectral Density
Tau_q_mat = [...
    dt^5/20,  dt^4/8    dt^3/6 ;
    dt^4/8,   dt^3/3,   dt^2/2 ;
    dt^3/6,   dt^2/2,   dt,    ];
Q = qC * Tau_q_mat;
    
% GPS Measurement Noise
simga_gps = 2.5; % [m]
R_gps = [simga_gps^2];


%% Generate Truth Data and Measurements

for k_imu = 1:K_imu
    
end

%% INS Implementation

for k_imu = 1:K_imu
    
    % Estimate Error State using Kalman Filter
    if ~mod(k_imu / k_gps, 1)
        
    end
    
end

%% Plot results