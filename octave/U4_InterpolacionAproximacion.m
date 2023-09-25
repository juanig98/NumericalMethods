addpath('./MetodosNumericos/');
clear;
clc;

% format long;
% disp("-----------Ejercicio 1-----------")
% x = [0, 1, 3];
% y = [-2, 6, 40];
% p = Lagrange2grado(x, y);
% disp(["\nResultado: P(x) = " num2str(polyout(p, 'x'))]);

% disp("-----------Ejercicio 2-----------")
% x = [-1 0 3 7];
% y = [2 0 4 7];
% p = Lagrange(x, y);
% disp(["\nResultado: P(x) = " num2str(polyout(p, 'x'))]);

% disp("-----------Ejercicio 3-----------")
% xi = 1989;
% x = [1987, 1988, 1990];
% y = [53, 71, 91];
% p = LagrangeEstimacion(xi, x, y);
% disp(["\nResultado: P(x) = " num2str(polyout(p, 'x'))]);

% format short;
% disp("-----------Ejercicio 4-----------")
% xi = 0;
% x = [-2, -1, 1, 2];
% y = [0, 1, 1, 0];
% % p = LagrangeEstimacion(xi, x, y);
% % disp(["\nResultado: P(x) = " num2str(polyout(p, 'x'))]);
% p = Lagrange(x, y);
% disp(["\nResultado: P(x) = " num2str(polyout(p, 'x'))]);
% disp(["\nP(0) = " num2str(polyval(p, xi))]);

% disp("-----------Ejercicio 5-----------")
% x = [1, 2, 3, 4];
% y = [3, -5, -6, -2];
% p = Lagrange(x, y);
% disp(["\nResultado: P(x) = " num2str(polyout(p, 'x'))]);

% disp("-----------Ejercicio 6-----------")
% x = [0.5, 1.2, 3.5];
% y = [2, 3, 5];
% p = Lagrange(x, y);
% disp(["\nResultado: P(x) = " num2str(polyout(p, 'x'))]);

% disp("-----------Ejercicio 7-----------")
% xi = 0.34
% x = [0.3, 0.32, 0.35];
% y = [0.29552, 0.31457, 0.34290];
% p = Lagrange(x, y)
% disp(["\nResultado: P(x) = " num2str(polyout(p, 'x'))]);
% disp(["\nP(sen(0.34)) = " num2str(polyval(p, xi))]);

% disp("-----------Ejercicio 8-1-----------")
% xi = 1.75;
% x = [1.7, 1.8, 1.9];
% y = [(4 * x(1) - 7) / (x(1) - 2), (4 * x(2) - 7) / (x(2) - 2), (4 * x(3) - 7) / (x(3) - 2)];
% p = Lagrange(x, y)
% disp(["\nResultado: P(x) = " num2str(polyout(p, 'x'))]);
% disp(["\nP(sen(1.75)) = " num2str(polyval(p, xi))]);

% % disp(["\n\tVERIFICACION utilizando polyfit"]);
% % c = polyfit(x, y, 2);
% % disp(["P(x) = " num2str(c)]);
% % disp(["f(1.75) = " num2str(polyval(c, 1.75))]);

% disp("-----------Ejercicio 8-2-----------")
% x = [1.7, 1.8, 1.9, 2.1];
% y = [(4 * x(1) - 7) / (x(1) - 2), (4 * x(2) - 7) / (x(2) - 2), (4 * x(3) - 7) / (x(3) - 2), (4 * x(4) - 7) / (x(4) - 2)];
% p = Lagrange(x, y)
% disp(["\nResultado: P(x) = " num2str(polyout(p, 'x'))]);
% disp(["\nP(sen(1.75)) = " num2str(polyval(p, xi))]);

% % disp(["\n\tVERIFICACION utilizando polyfit y polyval"]);
% % c = polyfit(x, y, 3);
% % disp(["P(x) = " num2str(c)]);
% % disp(["f(1.75) = " num2str(polyval(c, 1.75))]);

% disp("-----------Ejercicio 10-----------")
% xi = [300, 1700, 3300, 5300, 5900];
% x = [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000];
% y = [32, 176.0, 296.4, 405.7, 509.0, 608.4, 704.7, 799.0, 891.9, 983.0, 1072.6, 1160.8, 1247.5];

% for i = 1:length(xi)
%     disp(["\nemf = " num2str(xi(i)) "\t Temp (°F) = " num2str(FLAGR(xi(i), x, y))]);
% endfor

% disp("-----------Ejercicio 10-----------")

% xi = [18.27, 41, 52];
% x = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60];
% y = [0.9998679, 0.9999919, 0.9997277, 0.9991265, 0.9982323, 0.9970739, 0.9956756, 0.9940594, 0.9922455, 0.99024, 0.98807, 0.98573, 0.983241];

% for k = 2:3
%     p = polyfit(x, y, k);
%     disp(["\nPolinomio interpolador de grado " num2str(k) ": \n P(x) = " num2str(polyout(p, 'x'))]);

%     for i = 1:length(xi)
%         disp(["\nP(" num2str(xi(i)) ") = " num2str(polyval(p, xi(i)))]);
%     endfor

% endfor

% disp("-----------Ejercicio 12-----------")
% xi = [18.27, 41, 52];
% x = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60];
% y = [0.9998679, 0.9999919, 0.9997277, 0.9991265, 0.9982323, 0.9970739, 0.9956756, 0.9940594, 0.9922455, 0.99024, 0.98807, 0.98573, 0.983241];

% for k = 2:3
%     p = polyfit(x, y, k);
%     disp(["\nPolinomio interpolador de grado " num2str(k) ": \n P(x) = " num2str(polyout(p, 'x'))]);

%     for i = 1:length(xi)
%         disp(["\nP(" num2str(xi(i)) ") = " num2str(polyval(p, xi(i)))]);
%     endfor

% endfor

% disp("-----------Ejercicio 13-----------")
% x = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100];
% y = [1.5033, 1.4901, 1.4774, 1.4651, 1.4532, 1.4418, 1.4307, 1.4200, 1.4096, 1.3997, 1.3902, 1.3811, 1.3723, 1.3639, 1.3557, 1.3479, 1.3403,  1.3330];

% disp("\nIntepolacion considerando los primeros 9 valores");
% p = polyfit(x(1:9), y(1:9), 1);
% disp(["\tP(x) = " num2str(polyout(p, "x")) ]);

% disp("\nIntepolacion considerando los ultimos 9 valores");
% p = polyfit(x(9:18), y(9:18), 1);
% disp(["\tP(x) = " num2str(polyout(p, "x")) ]);

% disp("\nIntepolacion considerando los 10 valores intermedios");
% p = polyfit(x(4:14), y(4:14), 1);
% disp(["\tP(x) = " num2str(polyout(p, "x")) ]);

% disp("\nIntepolacion considerando los primeros 4 valores");
% p = polyfit(x(1:4), y(1:4), 1);
% disp(["\tP(x) = " num2str(polyout(p, "x")) ]);

% disp("\nIntepolacion considerando los ultimos 4 valores");
% p = polyfit(x(14:18), y(14:18), 1);
% disp(["\tP(x) = " num2str(polyout(p, "x")) ]);

% disp("-----------Ejercicio 14-----------")
% x = [-5, 0, 2, 3];
% y = [-2, 2, 4, 4];

% p = MinCuadradosLineales(x, y);
% disp(["\nRecta resultante = \n\n\t\t y = " num2str(polyout(p, 'x'))]);

disp("-----------Ejercicio 15-----------")
x = [1, 2, 3, 4, 5, 6, 7, 8, 9];
y = [2.1, 3.3, 3.9, 4.4, 4.6, 4.8, 4.6, 4.2, 3.4];

p = MinCuadradosParabola(x, y);
disp(["\nRecta resultante = \n\n\t\t y = " num2str(polyout(p, 'x'))]);
