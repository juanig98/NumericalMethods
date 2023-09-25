function [p] = MinCuadradosParabola(x, y)
    long = length(x);

    for i = 1:long
        x2(i) = x(i)^2;
        x3(i) = x(i)^3;
        x4(i) = x(i)^4;
        xy(i) = x(i) * y(i);
        x2y(i) = x(i)^2 * y(i);
    endfor

    disp(["x = \t" num2str(x)]);
    disp(["y = \t" num2str(y)]);
    disp(["x^2 = \t" num2str(x2)]);
    disp(["x^3 = \t" num2str(x3)]);
    disp(["x^4 = \t" num2str(x4)]);
    disp(["x*y = \t" num2str(xy)]);
    disp(["(x^2)*y  = \t" num2str(x2y)]);

    a(1, :) = [long, sum(x), sum(x2)];
    a(2, :) = [sum(x), sum(x2), sum(x3)];
    a(3, :) = [sum(x2), sum(x3), sum(x4)];
    a(3, :) = [sum(x2), sum(x3), sum(x4)];
    disp("A = ");
    disp(a);

    b(1, :) = [sum(y)];
    b(2, :) = [sum(xy)];
    b(3, :) = [sum(x2y)];
    b(3, :) = [sum(x2y)];
    disp("B = ");
    disp(b);

    p = linsolve(a, b);
endfunction
