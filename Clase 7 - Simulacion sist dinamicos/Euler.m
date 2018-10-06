function [ x, t ] = Euler( f, x0, h, T , beta, gamma)
t0 = T(1);
tf = T(2);

N = floor((tf-t0)/h); % Numero de pasos total
t = zeros(1,N);
x = zeros(3,N);

t(1) = t0;
x(:,1) = x0;

for n = 2:N
    x(:,n) = x(:,n-1) + h*f(x(:,n-1),beta,gamma);
    t(n) = t(n-1) + h;
end
end

