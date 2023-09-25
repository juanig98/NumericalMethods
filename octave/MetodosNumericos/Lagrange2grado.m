function [p] = Lagrange2grado(x, y)
    disp("x = ");
    disp(x);
    disp("y = ");
    disp(y);
    m = [1, -x(2) - x(3), x(2) * x(3); 1, -x(1) - x(3), x(1) * x(3); 1, -x(1) - x(2), x(1) * x(2)];

    disp("\nP(x) =");
    disp(m);

    m(1, :) = y(1) * m(1, :) / ((x(1) - x(2)) * (x(1) - x(3)));
    m(2, :) = y(2) * m(2, :) / ((x(2) - x(1)) * (x(2) - x(3)));
    m(3, :) = y(3) * m(3, :) / ((x(3) - x(1)) * (x(3) - x(2)));
    p = m(1, :) + m(2, :) + m(3, :);

    disp("\nP(x) =");
    disp(m);

    p
endfunction
