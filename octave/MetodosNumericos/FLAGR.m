function [val] = FLAGR(xi, x, y)
    long = length(x);
    [p, c] = Lagrange(x, y);
    val = polyval(p, xi);
endfunction
