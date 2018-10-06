%% Simulacion de un modelo de epidemias SIR
clc
close all

% Condiciones iniciales
S0 = 9990;
I0 = 10;
R0 = 0;
T0 = S0 + I0 + R0;

h = 0.1;

%% Caso 1 
%beta = 0.0001;
%gamma = 0.05;

beta = 0.0001;
gamma = 0.005;

% Euler
[ x_Euler, t ] = Euler( @SIR_model,[S0,I0,R0]' , h, [0,100] , beta, gamma);

%RK4
[ x_RK4, t ] = RK4( @SIR_model,[S0,I0,R0]' , h, [0,100] , beta, gamma);

figure
hold on
plot(t,x_Euler(2,:),'DisplayName','Euler')
plot(t,x_RK4(2,:),'DisplayName','RK4')
xlabel({'tiempo'});
ylabel({'Infectados'});
title({'CASO 1'});
legend('show');


%% Caso 2
beta = 0.001;
gamma = 0.1;

% Euler
[ x_Euler, t ] = Euler( @SIR_model,[S0,I0,R0]' , h, [0,100] , beta, gamma);

%RK4
[ x_RK4, t ] = RK4( @SIR_model,[S0,I0,R0]' , h, [0,100] , beta, gamma);

figure
hold on
plot(t,x_Euler(2,:),'DisplayName','Euler')
plot(t,x_RK4(2,:),'DisplayName','RK4')
xlabel({'tiempo'});
ylabel({'Infectados'});
title({'CASO 2'});
legend('show');

