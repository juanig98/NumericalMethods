addpath('./MetodosNumericos/');
clear;
clc;

% format long;
% disp("-----------Ejercicio 1a-----------")
% A = [3.333, 15920, -10.333; 2.222, 16.71, 6.612; 1.5611, 5.1791, 1.6852];
% b = [15913; 28.544; 8.4254];
% GaussElim(A, b, true);

% disp("-----------Ejercicio 1b-----------")
% format short;
% A = [1, 1/2, 1/3; 1/2, 1/3, 1/4; 1/3, 1/4, 1/5];
% b = [2; -1; 0];
% GaussElim(A, b, true);

% disp("-----------Ejercicio 1c-----------")
% A = [1 2 -12 8; 5 4 7 -2; -3 7 9 5; 6 -12 -8 3];
% b = [27; 4; 11; 49];
% GaussElim(A, b, true);

% disp("-----------Ejercicio 2a-----------")
% A = [0, 2, 0, 1; 2, 2, 3, 2; 4, -3, 0, 1; 6, 1, -6, -5];
% b = [0; -2; -7; 6];
% GaussJordan(A, b, true);

% disp("-----------Ejercicio 2b-----------")
% A = [1, 2, -4; 2, 5, 2; 4, 1, -1];
% b = [11; 3; 6];
% GaussJordan(A, b, true);

% disp("-----------Ejercicio 3-----------")
% A = [
%       -1.41, 2, 0;
%       1, -1.41, 1;
%       0, 2, -1.41
% ];
% b = [1; 1; 1];
% GaussElim(A, b, true);
% GaussJordan(A, b, true);

% format short;
% disp("-----------Ejercicio 4-----------")
% A = [
%     20, 25, 40, 50;
%     10, 15, 20, 22;
%     10, 8, 10, 15;
%     3, 4, 7, 20
%     ];
% b = [
%     1970;
%     970;
%     601;
%     504
%     ];
% GaussJordan(A, b, true);

% disp("-----------Ejercicio 5a-----------")
% A = [
%     2, -1, 1;
%     3, 3, 9;
%     3, 3, 5
%     ];
% b = [
%     0;
%     16.5;
%     12.5
%     ]
% LU(A, b);

% disp("-----------Ejercicio 5b-----------")
% A = [
%     1, 0.333, 1.5, -0.333;
%     -2.01, 1.45, 0.5, 2.95;
%     4.32, -1.95, 0, 2.08;
%     5.11, -4, 3.333, -1.11
%     ];
% b = [
%     3;
%     5.4;
%     0.13;
%     3.77
%     ];
% LU(A, b);

% disp("-----------Ejercicio 8a-----------")
% A = [
%     4, 0.24, -0.08;
%     0.09, 3, -0.15;
%     0.04, -0.08, 4
%     ];
% b = [
%     8;
%     9;
%     20
%     ];
% err = 0.01;
% nmax = 5;
% Jacobi(A, b, err, nmax);

% disp("-----------Ejercicio 8b-----------")
% A = [
%     10, -1, 2, 0;
%     -1, 11, -1, 3;
%     2, -1, 10, -1;
%     0, 3, -1, 8
%     ];
% b = [
%     6;
%     25;
%     -11;
%     15
%     ];
% err = 0.001;
% nmax = 10;
% Jacobi(A, b, err, nmax);



% disp("-----------Ejercicio 9a-----------")
% A = [
%     1, 7, -3;
%     4, -4, 9;
%     12, -1, 3
%     ];
% b = [
%     -51;
%     61;
%     8
%     ];
% err = 0.001;
% nmax = 6;
% GaussSeidel(A, b, err, nmax);

% disp("-----------Ejercicio 9b-----------")
% A = [
%     3, 1, 1;
%     1, 5, 2;
%     1, 2, 5
%     ];
% b = [
%     10;
%     21;
%     30
%     ];
% err = 0.001;
% nmax = 7;
% GaussSeidel(A, b, err, nmax);
