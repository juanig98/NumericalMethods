addpath('./MetodosNumericos/');
clear;
clc;

format long;
% disp("-----------Ejercicio 1-----------");
% func = @(x) x^3 - 17;
% a = 2;
% b = 3;
% err = 0.0125;
% iter = 10
% Biseccion(func, a, b, err, iter, true);

% disp("-----------Ejercicio 2-----------");
% func = @(x) x^2 - sin(x);
% a = 0.1;
% b = 1.57;
% err = 0.001;
% iter = 50
% format long;
% Biseccion(func, a, b, err, iter, true);

% disp("-----------Ejercicio 3-----------");
% func = @(x) sin(x) - e^(-x);
% a = 0.5;
% b = 1;
% err = 0.00001;
% iter = 50;
% format long;
% RegulaFalsi(func, a, b, err, iter, true);

% disp("-----------Ejercicio 4-----------");
% func = @(x) x^3 - x + 1 - 2 * x^2;
% a = 0.5;
% b = 2;
% err = 0.0001;
% iter = 50;
% format long;
% RegulaFalsi(func, a, b, err, iter, true);

% disp("-----------Ejercicio 5-----------");
% func = @(x) e^x - 2;
% a = 0;
% b = 2;
% err = 0.01;
% iter = 50;
% format long;
% RegulaFalsi(func, a, b, err, iter, true);

% disp("-----------Ejercicio 6-----------");
% func = @(x) -19 * (x - 0.5) * (x - 1) +e^x + e^(-2 * x);
% err = 0.001;
% iter = 10;
% format long;

% for i=-10:9
%     a = i;
%     b = i + 1;
%     printf("\n\nEn el intervalo [%d, %d]", a, b);
%     [sol, numIter, error, c] = RegulaFalsi(func, a, b, err, iter, false, true);
%     if sol
%         printf("\tHay solución");
%     else
%         printf("\tNo hay solución");
%     end
%     printf("\n\n")
% end

% TODO: REVISAR!
% disp("-----------Ejercicio 7i-----------");
% f = @(x) e^x - 5 * x^2;
% fdx = @(x) e^x - 5 * x;
% err = 0.001;
% iter = 50;
% a = -5
% Newton(f, fdx, a, err, iter, true)

% disp("-----------Ejercicio 7ii-----------");
% f = @(x) x^3 - 2 * x - 1;
% xn = 2.4;
% xn_1 = 2.5;
% err = 0.001;
% iter = 20;
% Secante(f, xn_1, xn, err, iter, true);

% disp("-----------Ejercicio 7iii-----------");
% f = @(x) sqrt(x) + 2 - x;
% a = 3.5;
% b = 5.5;
% err = 0.00001;
% iter = 20;
% RegulaFalsi(f, a, b, err, iter, true);

% disp("-----------Ejercicio 8-----------");
% f = @(x) x^3 - 3 * x + 1;
% p0 = 1;
% p1 = 1.5;
% p2 = 2;
% err = 0.001;
% iter = 20;
% Muller(f, p0, p1, p2, err, iter, true);
