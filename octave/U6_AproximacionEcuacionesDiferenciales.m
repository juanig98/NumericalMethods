addpath('./MetodosNumericos/');
clear;
clc;

format long;
% disp("-----------Ejercicio 1a-----------")
% f = @(y, t) -20 * y + 7 * e^(-0.5 * t);
% a = 0;
% b = 0.02;
% y0 = 5;
% h = 0.01;
% R = Euler(f, a, b, y0, h, true);

% disp("-----------Ejercicio 1b-----------")
% f = @(y, t) -20 * y + 7 * e^(-0.5 * t);
% fAnalitica = @(t) 5 * e^(-20 * t) + (7/19.5) * (e^(-0.5 * t) - e^(-20 * t));
% a = 0;
% b = 0.09;
% y0 = 5;
% disp("-----------con h=0.01-----------")
% h = 0.01;
% R = Euler(f, a, b, y0, h, true, fAnalitica);
% disp("-----------con h=0.001-----------")
% h = 0.001;
% R = Euler(f, a, b, y0, h, true, fAnalitica);
% disp("-----------con h=0.0001-----------")
% h = 0.00024; # Máximo posible de achicar
% R = Euler(f, a, b, y0, h, true, fAnalitica);

% disp("-----------Ejercicio 2-----------")
% disp("-----------Ejercicio 3-----------")
% f = @(y) -y^(1.5) + 1;
% a = 0;
% b = 1;
% y0 = 10;
% h = 0.1;
% EulerMejorado(f, a, b, y0, h, true);

% disp("-----------Ejercicio 6-----------")
% f = @(y, t) t * y + 1;
% a = 0;
% b = 5;
% y0 = 0;
% h = 0.2;
% RungeKutta4(f, a, b, y0, h, true);

% disp("-----------Ejercicio Random-----------")
% f = @(y, t) 2 * t + y;
% a = 0;
% b = 1;
% y0 = 1;
% h = 0.2;
% RungeKutta4(f, a, b, y0, h, true);

disp("-----------Ejercicio adicionales-----------")
disp("-----------Ejercicio 1-----------")
a = 0;
b = 5;

disp("-----------Ejercicio 1a-----------")
% f = @(y, t) -t * y + 1;
% y0 = 1;
% disp("-----------Con h=0.5-----------")
% h = 0.5;
% R = Euler(f, a, b, y0, h, true);
% disp("-----------Con h=0.01-----------")
% h = 0.01;
% R = Euler(f, a, b, y0, h, true);

% disp("-----------Ejercicio 1b-----------")
% f = @(y, t) -3 * y + e^(-t);
% y0 = 1;
% disp("-----------Con h=0.5-----------")
% h = 0.5;
% R = Euler(f, a, b, y0, h, true);
% disp("-----------Con h=0.01-----------")
% h = 0.01;
% R = Euler(f, a, b, y0, h, true);

% disp("-----------Ejercicio 1c----------")
% f = @(y, t) t^2 - y;
% y0 = 0.5;
% disp("-----------Con h=0.5-----------")
% h = 0.5;
% R = Euler(f, a, b, y0, h, true);
% disp("-----------Con h=0.01-----------")
% h = 0.01;
% R = Euler(f, a, b, y0, h, true);

% disp("-----------Ejercicio 1d----------")
% f = @(y) -(y * abs(y));
% y0 = 0.5;
% disp("-----------Con h=0.5-----------")
% h = 0.5;
% R = Euler(f, a, b, y0, h, true);
% disp("-----------Con h=0.01-----------")
% h = 0.01;
% R = Euler(f, a, b, y0, h, true);

% disp("-----------Ejercicio 1e----------")
% f = @(y, t) sin(t) - abs(y^(1/2));
% y0 = 1;
% disp("-----------Con h=0.5-----------")
% h = 0.5;
% R = Euler(f, a, b, y0, h, true);
% disp("-----------Con h=0.01-----------")
% h = 0.01;
% R = Euler(f, a, b, y0, h, true);

disp("-----------Ejercicio 3----------")
a = 0;
b = 5;
disp("-----------Ejercicio 3a----------")
f = @(y, t) (-4 * y^2) / (1/2 * t);
y0 = 0;
disp("-----------Con h=0.5-----------")
h = 0.01;
R = Euler(f, a, b, y0, h, true);
