% Función para generar muestras de una variable aleatoria discreta Binomial
% con parametros N y p
function [] = Gen_Binomial(N_muestras, N, p)
% N_muestras: Número de muestras
% N: repeticiones
% p: Probabilidad de éxito (1). Notar que (1-p) es la probabilidad de
% fracaso

x = zeros(1, N_muestras);
% Loop para sumar N variables de Bernoulli
for n=1:N
    x = x + Bernoulli(N_muestras, p);
end

% Mostramos histograma del resultado
figure
n_casos = zeros(1,N);
for k=0:N-1
   n_casos(k+1) = sum(x==k);
end 
bar(0:N-1,n_casos)

end

function z = Bernoulli(N, p)
% N: Número de muestras
% p: Probabilidad de éxito (1). Notar que (1-p) es la probabilidad de
% fracaso
x = rand(1,N); % Genero N muestras uniformes en [0,1]
z = zeros(1,N); % Aqui se guardaran las muestras de Bernoulli.
z(x < p) = 1; % Aigno 1 con probabilidad p
end

