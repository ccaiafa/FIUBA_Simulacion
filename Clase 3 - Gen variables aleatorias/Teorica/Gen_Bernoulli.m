% Función para generar muestras de una variable aleatoria discreta de
% Bernoulli
function [] = Gen_Bernoulli(N, p)
% N: Número de muestras
% p: Probabilidad de éxito (1). Notar que (1-p) es la probabilidad de
% fracaso
x = rand(1,N); % Genero N muestras uniformes en [0,1]
z = zeros(1,N); % Aqui se guardaran las muestras de Bernoulli.
z(x < p) = 1; % Aigno 1 con probabilidad p

% Mostramos histograma del resultado
figure
n_casos_1 = sum(z); % Nro de casos k = 1
n_casos_0 = N-sum(z); % Nro de casos k=0
k = [0,1]; p = [n_casos_0 n_casos_1]; 
bar(k,p)

end

