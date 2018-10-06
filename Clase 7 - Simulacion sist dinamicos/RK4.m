function [ x, t ] = RK4( f, x0, h, T , beta, gamma)
t0 = T(1);
tf = T(2);

N = floor((tf-t0)/h); % Numero de pasos total
t = zeros(1,N);
x = zeros(3,N);

t(1) = t0;
x(:,1) = x0;

for n = 2:N
    k1 = h*f(x(:,n-1),beta,gamma);
    k2 = h*f(x(:,n-1) + 0.5*k1,beta,gamma);
    k3 = h*f(x(:,n-1) + 0.5*k2,beta,gamma);
    k4 = h*f(x(:,n-1) + k3,beta,gamma);
    x(:,n) = x(:,n-1) + (1/6)*(k1 + 2*k2 + 2*k3 + k4);
    t(n) = t(n-1) + h;
end
end

