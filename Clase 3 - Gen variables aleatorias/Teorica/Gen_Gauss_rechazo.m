% Función para generar muestras de una variable aleatoria con distribución
% Gaussiana usando el método de aceptación/rechazo (Libro [16])
function [] = Gen_Gauss_rechazo(N)
% N: Número de muestras
c = sqrt(2*exp(1)/pi); % Ver Libro [16, pag. 77]
%% Paso 1: Generamos muestras de la variable exponencial Y, media 1
t = exprnd(1,1,N); % Generamos un vector de 1xN muestras
p = fX(t)./(c*fY(t)); % Probabilidad de aceptar
z= [];
for n=1:N
    r = rand();
    if r < p(n) % acepto t(n) con prob. p(n)
        r2 = rand();
        if r2 < 0.5 % con prob 0.5 lo dejo positivo
            z = [z, t(n)];
        else  % con prob 0.5 lo hago negativo
            z = [z, -t(n)];
        end
    end 
end

disp(['Porcentaje de rechazo = ', num2str((N-length(z))/N)])

% Mostramos histograma del resultado
figure
histogram(z,100)
title('histograma de Z')

end

% pdf Exponencial (media=1)
function f = fY(y)
f = exp(-y);
end

% pdf Gaussiana (media=0, desvio=1)
function f = fX(x)
f = exp(-x.^2/2)/sqrt(2*pi);
end