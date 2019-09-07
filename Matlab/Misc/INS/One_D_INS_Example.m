%% INS_simulation
% 
% Simulation of estimating a trajectory of an object using a GPS aided
% Inertial Navigation System. Based on the thesis by Eduardo Infante
% "Development and Assessment of Loosely-Coupled INS Using Smartphone
% Sensors"
% 
% @author: Matt Marti
% @date: 2019-03-09

clear, clc, clear global


%% Parameters
% Refer to the notebook for the models

% Parameters
nx = 27; % Dimension of error state
ny = 22; % Dimension of INS state
nv = 18; % Number of noise terms in error state
nvy = 6; % Number of noise terms for manuevering noise
nz_IMU = 6; % Number of measurements for IMU
nz_GPS = 6; % Number of measurements for GPS
nInt = 10; % Number of integration steps

% Measurement Times
dt_IMU = .01;.04; % IMU Sampling time period
dt_GPS = 1; % GPS Sampling time period
tof = 25; % Time Of Flight
Nx = round(tof / dt_IMU); % Number of IMU Samples
Nz_IMU = Nx; % Number of IMU observations
Nz_GPS = round(tof / dt_GPS); % Number of GPS observations

% INS Bias/Scale Factor Paremters
del_biasacc = 1e-4*(2*rand(3,1)-1);  % Acc Bias Rate
del_biasgyr = 1e-5*(2*rand(3,1)-1); % Gyr Bias Rate
init_biasacc = 1e-3*(2*rand(3,1)-1); % Acc Bias
init_biasgyr = 1e-4*(2*rand(3,1)-1); % Gyr Bias
scaleacc = 1e-7*(2*rand(3,1)-1); % Acc Scale Factor
scalegyr = 1e-6*(2*rand(3,1)-1); % Gyr Scale Factor

% INS Bias/Scale Factor Time Constants
beta_a = 1e-4;1e-2;
beta_g = 1e-4;1e-2;
beta_ba = 1e-4;1e-2;
beta_bg = 1e-4;1e-2;
beta_sa = 1e-4;1e-2;
beta_sg = 1e-4;1e-2;

% INS Noise Standard Deviations
sigma_a = 1e-3;
sigma_g = 1e-3;
sigma_ba = 1e-3;
sigma_bg = 1e-3;
sigma_sa = 1e-3;
sigma_sg = 1e-3;

% Initial INS state
y0 = zeros(ny,1);
y0(1:3,1) = 6400e3*[1; 0; 0]; % Position at lat / lon = 0,0
y0(6) = 0.25; % Northward velocity
q = [1; 1; 1; 1]; % Set heading, pitch, roll to 0
q = q/norm(q); % Normalize quaternion
y0(7:10,1) = q; % Set Attitude

% IMU Mechanization function = [ xkp1, latlonalt, attitude, acc, gyr ]
deltaflag = 0;
R_b_m = eye(3);
g = @(y, z) imuMechanization( dt_IMU, y, z, R_b_m, deltaflag );

% F - Dynamics Propagation function (Error State)
f = @(k, x, v, y, zIMU) insErrorDynamicsModel( ...
        dt_IMU, x, v, y, zIMU, beta_ba, beta_bg, beta_sa, beta_sg, nInt );

% H - Measurement Model
h = @(k, x) insErrorMeasurementModel_GNSS_rv( x, zeros(nz_GPS,1) );

% IMU dynamics covariance (noise for manuevering)
Qy = zeros(nvy,nvy);
Qy(1,1) = 1e-7; % Accel
Qy(2,2) = 1e-4; % Accel
Qy(3,3) = 1e-7; % Accel
Qy(4,4) = 1e-6; % Gyro
Qy(5,5) = 1e-6; % Gyro
Qy(6,6) = 1e-4; % Gyro

% R - Measurement Noise Covariance
R_GPS = diag([5;5;7;.1;.1;.2]);
R_IMU = diag([1e-4;1e-4;1e-4;1e-3;1e-3;1e-3]);

% Q - Process Noise Covariance
Q = zeros(nv,nv);
Q(1:3,1:3) = 2*sigma_a^2*beta_a*eye(3);
Q(4:6,4:6) = 2*sigma_g^2*beta_g*eye(3);
Q(7:9,7:9) = 2*sigma_ba^2*beta_ba*eye(3);
Q(10:12,10:12) = 2*sigma_bg^2*beta_bg*eye(3);
Q(13:15,13:15) = 2*sigma_sa^2*beta_sa*eye(3);
Q(16:18,16:18) = 2*sigma_sg^2*beta_sg*eye(3);


%% Generate Trajectory time history

% Generate IMU True Manuevering Noise
Sq_vy = chol(Qy)';
vyhist = Sq_vy*randn(nvy,Nx);

% Preallocate
yhist = zeros(ny,Nx);
yhist(:,1) = y0;
zyhist = zeros(nvy,Nx);
hprhist = zeros(3,Nx);

% Generate data
zk = zeros(nz_IMU,1);
progressbar = waitbar(0, 'Generating Trajectory');
for kp1 = 2:Nx
    k = kp1 - 1;
    
    % Partition Dynamics vector
    yk = yhist(:,k);
    zk = zk + vyhist(:,k);
    q = yk(7:10);
    zk(1:3) = zk(1:3) - quat2dircos(q)'*gravitymodel(yk(1:3),q); % Not in free fall
    
    % State Propagation
    [ ykp1, latlonalt, attitude, acc, gyr ] = g(yk,zk);
    
    % Partition k+1 state
    yhist(:,kp1) = ykp1;
    hprhist(:,kp1) = attitude;
    
    % Iterate
    zyhist(:,k) = zk;
    if ~mod(kp1/Nx*100-1,1), waitbar(kp1/Nx, progressbar); end
end
close(progressbar);


%% Generate Measurement Time Historys

% Generate INS True Measurment Noise
Sr_IMU = chol(R_IMU)';
whist_IMU = Sr_IMU*randn(nz_IMU,Nz_IMU);

% Generate INS True Measurment Noise
Sr_GPS = chol(R_GPS)';
whist_GPS = Sr_GPS*randn(nz_GPS,Nz_GPS);

% Generate True Process Noise (Error State)
Sq = chol(Q)';
v0 = Sq*randn(nv,1);
vhist = Sq*randn(nv,Nz_GPS);

% Generate IMU Measurement Noise
Sr_IMU = chol(R_IMU);
wyhist = Sr_IMU *randn(nz_IMU,Nz_IMU);

% Preallocate
zhist_IMU = zeros(nz_IMU,Nz_IMU);
zhist_GPS = zeros(nz_GPS,Nz_GPS);

% Initial values
wkp1_GPS = whist_GPS(:,1);
zhist_GPS(:,1) = yhist(1:6,1) + wkp1_GPS;

% Generate data
progressbar = waitbar(0, 'Generating Measurements');
kp1gps = 1;
for kp1 = 2:Nx+1
    gpsflag = ~mod(kp1,round(dt_GPS/dt_IMU));
    k = kp1 - 1;
    
    % IMU state components
    yk = yhist(:,k);
    
    % IMU Measurement Noise
    wk = wyhist(:,k);
    
    % IMU measurements, apply parameters and noise
    acc = zyhist(1:3,k) + wk(1:3);
    gyr = zyhist(4:6,k) + wk(4:6);
    ba = init_biasacc + k*dt_IMU*del_biasacc;
    bg = init_biasgyr + k*dt_IMU*del_biasgyr;
    sfa = scaleacc;
    sfg = scalegyr;
    za = (1 + sfa) .* (acc + ba);
    zg = (1 + sfg) .* (gyr + bg);
    zhist_IMU(:,k) = [za; zg];
    
    % Update true bias / scale factors
    yk(11:13) = ba;
    yk(14:16) = sfa;
    yk(17:19) = bg;
    yk(20:22) = sfg;
    yhist(:,k) = yk;
    
    % GPS Observation
    if gpsflag
        wkp1_GPS = whist_GPS(:,kp1gps);
        zhist_GPS(:,kp1gps) = yhist(1:6,kp1) + wkp1_GPS;
    end
    
    % Iterate
    if gpsflag, kp1gps = kp1gps + 1; end
    if ~mod(kp1/Nx*100-1,1), waitbar(kp1/Nx, progressbar); end
end
close(progressbar);


%% Run Filter on Time History


%% Plot

% Ground Track Plot
figure(1)
hold off
plot(yhist(2,:)-yhist(2,1), yhist(3,:)-yhist(3,1), ...
    'k.-', 'linewidth', 1.25, 'markersize', 10);
hold on
plot(yhathist(2,:)-yhist(2,1), yhathist(3,:)-yhist(3,1), ...
    'b.-', 'linewidth', 1.25, 'markersize', 10);
plot(zhist_GPS(2,:)-yhist(2,1), zhist_GPS(3,:)-yhist(3,1), ...
    'ro', 'markersize', 5);
title('Object Ground Track');
xlabel('ECEF Y');
ylabel('ECEF Z');
legend({'True', 'Kalman', 'GPS'});
grid on, grid minor

% Innovation Statistic Plot
figure(2);
hold off;
semilogy(epsilonhist', 'linewidth', 1.5);
hold on;
semilogy(r1nu*ones(size(epsilonhist)), 'r--', 'linewidth', 1.75);
semilogy(r2nu*ones(size(epsilonhist)), 'r--', 'linewidth', 1.75);
semilogy(r1nu_mean*ones(size(epsilonhist)), 'm--', 'linewidth', 1.75);
semilogy(r2nu_mean*ones(size(epsilonhist)), 'm--', 'linewidth', 1.75);
semilogy(mean(epsilonhist)*ones(size(epsilonhist)), 'b-.', ...
    'linewidth', 1);
semilogy(nz*ones(size(epsilonhist)), 'k-.', 'linewidth', 1);
hold off;
title('Innovation Statistic Consistency Test Time History');
ylabel('Innovation Statistic');
xlabel('Index of Innovation Statistic k');
grid on, grid minor;

% Attitude Error
figure(3);
hold off
attdiff = hprhathist - hprhist;
for i = 1:size(attdiff,2)
    if attdiff(1,i) > 180
        attdiff(1,i) = attdiff(1,i) - 360;
    elseif attdiff(1,i) < -180
        attdiff(1,i) = attdiff(1,i) + 360;
    end
end
plot(attdiff');
hold on
title('Attitude Error Time History');
legend({'H', 'P', 'R'});
grid on, grid minor

% Acceleration Bias
figure(4);
hold off
plot(yhist(11:13,:)', 'r');
hold on
plot(yhathist(11:13,:)', 'b');
title('Acceleration Bias Time History');
legend({'True', '', '', 'Kalman', '', ''});
grid on, grid minor

% Gyro Bias
figure(5);
hold off
plot(yhist(17:19,:)', 'r');
hold on
plot(yhathist(17:19,:)', 'b');
title('Gyro Bias Time History');
legend({'True', '', '', 'Kalman', '', ''});
grid on, grid minor

% Position Error
figure(6);
hold off
plot((yhathist(1:3,:) - yhist(1:3,:))');
title('Position Error Time History');
grid on, grid minor

% Velocity Error
figure(7);
hold off
plot((yhathist(4:6,:) - yhist(4:6,:))');
title('Velocity Error Time History');
grid on, grid minor

% Acceleration Error
figure(8);
hold off
plot((yhathist(7:9,:) - yhist(7:9,:))');
title('Acceleration Error Time History');
grid on, grid minor

% Acceleration Bias Error
figure(9);
hold off
plot(yhathist(11:13,:)' - yhist(11:13,:)');
title('Acceleration Bias Error Time History');
grid on, grid minor

% Gyro Bias Error
figure(10);
hold off
plot(yhathist(17:19,:)' - yhist(17:19,:)');
title('Gyro Bias Error Time History');
grid on, grid minor

% Covariance condition number
condhist = zeros(size(Phist,3),1);
for i = 1:length(condhist)
    condhist(i) = cond(squeeze(Phist(:,:,i)));
end
figure(11);
hold off
semilogy(condhist');
title('Covariance Condition Number Time History');
grid on, grid minor

% Estimated state error and measured state error
figure(12);
hold off
plot(zhist_Error(1:3,:)', 'r');
hold on
plot(xhathist(1:3,:)', 'b');
title('Error state');
legend({'Measured', '', '', 'Estimated', '', ''});
grid on, grid minor