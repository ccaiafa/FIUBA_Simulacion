% Script para generar muestras de una variable aleatoria exponencial a
% partir de una distribucion uniforme en [0,1] utilizando el método de la
% transformación inversa

N = 10000; % Número de muestras
lambda =1; % Parámetro de la distribución exponencial

%% Paso 1: Generamos muestras de la variable uniforme U
u = rand(1,N); % Generamos un vector de 1xN muestras

% Mostramos histograma de la distribución uniforme
figure
histogram(u,100)
title('histograma de U')


%% Paso 2: Aplicar la transformacion inversa
x = -log(1-u)/lambda; % Transformación inversa

% Mostramos histograma del resultado
figure
histogram(x,100)
title('histograma de X')