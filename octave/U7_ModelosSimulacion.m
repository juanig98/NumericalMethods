addpath("./MetodosNumericos")
clear;
clc;

% disp("-----------Ejercicio 5-----------")
% SiMec()

% disp("-----------Ejercicio 6a-----------")
% ut = 5000;
% t0 = 0;
% tf = 500;
% x0 = 12000;
% y0 = 600;
% r = 0.001;
% s = 0.01;
% a = 0.000002;
% b = 0.000001;
% SiBio(ut, t0, tf, x0, y0, r, s, a, b);

% lotkaVolterra()
% disp("-----------Ejercicio 6b-----------")
% ut = 5000;
% t0 = 0;
% tf = 500;
% x0 = 10000;
% y0 = 500;
% r = 0.001;
% s = 0.01;
% a = 0.000002;
% b = 0.000001;
% SiBio(ut, t0, tf, x0, y0, r, s, a, b);
% ut Número de iteraciones.
% t0 Tiempo inicial
% tf Tiempo final
% r Coeficiente de la razón de crecimiento de presas P.
% s Coeficiente de la razón de muerte de depredador D.
% a Constante de proporcionalidad que mide el número de interacciones presa-depredador en la que la presa es devorada.
% b Constante de proporcionalidad que mide el beneficio a la población de depredadores D de una presa P devorada.

disp("-----------Ejercicio 6b-----------")
ut = 5000;
t0 = 0;
tf = 3000;
x0 = 10000;
y0 = 40;
r = 0.08;
s = 0.02;
a = 0.001;
b = 0.00002;
SiBio(ut, t0, tf, x0, y0, r, s, a, b);
