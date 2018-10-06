function [ xp ] = SIR_model(x, beta, gamma )
% x(1) = S, x(2) = I,  x(3) = R

xp = zeros(3,1);
xp(1) = -beta*x(1)*x(2);
xp(2) = beta*x(1)*x(2) - gamma*x(2);
xp(3) = gamma*x(2);

end

