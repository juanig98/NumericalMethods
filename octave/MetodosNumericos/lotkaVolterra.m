% Lokta - Volterra - Modelo Presa Predador
xmin = 0;
xmax = 10;
ymin = 0;
ymax = 10;
tmin = 0;
dt = 0.1;

global params;
disp('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~');
disp('Este script resuelve el sistema clasico Presa-Predador de Lokta Volterra');
disp(' u�� = au - buv ');
disp(' v�� = -cv + duv');
disp('Ingresamos a, b, c, d positivos');
params = input('Ingresar constantes [ a b c d ] : ');
x0 = input('Ingresar condiciones iniales [x0 y0]: ');
tmax = input('Ingresar tiempo maximo: ');

eq = [0 0];
eq = [eq; params(3) / params(4) params(1) / params(2)];
disp("Puntos de equilibrio: ");
disp(eq);

disp("Condiciones inicales: ");
disp(x0);

dx = abs(xmax - xmin) / 30;
dy = abs(ymax - ymin) / 30;
escala = 0.027 * max(abs(xmax - xmin), abs(ymax - ymin));

t = tmin:dt:tmax;

function xdot = dsys(x, t)
    global params;
    u = x(1);
    v = x(2);
    xdot(1) = params(1) * u - params(2) * u * v;
    xdot(2) = -params(3) * v + params(4) * u * v;
endfunction

setax = [xmin xmax ymin ymax];
axis(setax)
[X, Y] = meshgrid(xmin:dx:xmax, ymin:dy:ymax);
DX = params(1) * X - params(2) * X .* Y;
DY = -params(3) * Y + params(4) * X .* Y;
L = sqrt(DX.^2 + DY.^2);
titulo = ["Fase vertical. Condiciones iniciales : x0= " num2str(x0(1)) " , y0= " num2str(x0(2))];
quiver(X, Y, escala * DX ./ L, escala * DY ./ L)

hold on;
plot(eq(:, 1), eq(:, 2), '*k')

x = lsode("dsys", x0, t);

plot(x(1, 1), x(2, 1), '*k', x(1, :), x(2, :), '-r')
hold off;
disp('presione una tecla para continuar...');
pause();

titulo = ["Historial de tiempo condiciones inicales: x0 = " num2str(x0(1)) ", y0=" num2str(x0(2))];
title(titulo)
plot(t, x(:, 1), '-r;x(t);', t, x(:, 2), '-g;y(t);')
pause();
