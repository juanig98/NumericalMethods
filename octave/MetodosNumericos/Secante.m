function [c, error, numIter] = Secante(func, x0, x1, tol, maxIter, proc)
    % Esta funcion genera una aproximacion de la raiz c de la
    %   funcion derivable f(x)  mediante el metodo de la secante.
    % Datos necesarios para llamar a la funcion:
    %   func, expresion de f(x);
    %   x0, primer valor a aproximar;
    %   x1, segundor valor a aproximar;
    %   tol, tolerancia maxima de error;
    %   maxIter, numero maximo de iteraciones;
    %   proc, (0 si no se desea mostrar el proceso de aproximacion, 1 si se desea ver el proceso de aproximacion)
    % La funcion devuelve como respuesta tres valores:
    %      c = valor aproximado de la rai�z;
    %      err = |f(c)|;
    %      numIter = numero de iteraciones realizadas.

    n = 0;
    error = abs(((x1 - x0) / x0) * 100);

    while error >= tol && n < maxIter
        n++;
        x2 = ((x0 * feval(func, x1)) - (x1 * feval(func, x0))) / (feval(func, x1) - feval(func, x0));
        error = abs(((x1 - x0) / x0) * 100);

        if proc == 1
            printf("\n\n------- Iteración N° %d", n)
            printf("\n\tx0 = %d", x0)
            printf("\n\tf(x0) = %d", feval(func, x0))
            printf("\n\tx1 = %d", x1)
            printf("\n\tf(x1) = %d", feval(func, x1))
            printf("\n\tx2 = %d", x2)
            printf("\n\tf(x2) = %d", feval(func, x2));
            printf("\nError = %d", error);
        endif

        x0 = x1;
        x1 = x2;
    endwhile

    if n > maxIter
        warning(["\nEl metodo de la secante falla despues de " num2str(n) " iteraciones\n"]);
    endif

    c = x2;
    numIter = n;

    if proc
        printf("\n\nSolución = %d\n\n", c);
    end

endfunction
