function [recta] = MinCuadradosLineales(x, y)
    long = length(x);

    for i = 1:long
        x2(i) = x(i)^2;
        xy(i) = x(i) * y(i);
    endfor

    msumx2sumx = ((long * sum(x2)) - (sum(x)^2));

    a0 = ((sum(x2) * sum(y)) - (sum(xy) * sum(x))) / msumx2sumx;

    a1 = ((long * sum(xy)) - (sum(x) * sum(y))) / msumx2sumx;

    disp(["x = " num2str(x)]);
    disp(["y = " num2str(y)]);
    disp(["x^2 = " num2str(x2)]);
    disp(["x*y = " num2str(xy)]);

    disp(["\nCalculo del termino independiente: \n a0 = ( ( " num2str(sum(x2)) " * " num2str(sum(y)) " ) - ( " num2str(sum(xy)) " * " num2str(sum(x)) " ) ) / ( ( " num2str(long) " * " num2str(sum(x2)) " ) -( " num2str(sum(x)^2) " ) ) "]);
    disp(["\nCalculo de la dependiente: \n a1 = ( ( " num2str(long) " * " num2str(sum(xy)) " ) - ( " num2str(sum(x)) " * " num2str(sum(y)) " ) ) / ( ( " num2str(long) " * " num2str(sum(x2)) " ) -( " num2str(sum(x)^2) " ) ) "]);

    recta = [a1 a0];
endfunction
