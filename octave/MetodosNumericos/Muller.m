function [sol, numIter, error, c] = Muller(func, p0, p1, p2, tol, numMaxIter, proc = false)
    % Esta funcion genera una aproximacion de la raiz c de la
    %   funcion derivable f(x) por los valor p0, p1 y p2 mediante el metodo de Muller.
    % Datos necesarios para llamar a la funcion:
    %   func, expresion de f(x);
    %   p0, valor de xn-2;
    %   p1, valor de xn-1;
    %   p2, valor de xn;
    %   tol, tolerancia maxima de error;
    %   numMaxIter, numero maximo de iteraciones;
    % La funcion devuelve como respuesta tres valores:
    %      c = valor aproximado de la rai�z;
    %      err = |f(c)|;
    %      numiter = numero de iteraciones realizadas.
    %      sol = (1 si existe raiz en [a,b], 0 si no existe raiz en el intervalo [a,b] por los criterios buscados

    sol = 0;
    h1 = p1 - p0;
    h2 = p2 - p1;
    d1 = (feval(func, p1) - feval(func, p0)) / h1;
    d2 = (feval(func, p2) - feval(func, p1)) / h2;
    d = (d1 - d2) / (h2 + h1);
    n = 3;

    while n <= numMaxIter

        b = d2 + h2 * d;
        func_d = (b^2 - 4 * feval(func, p2) * d)^(1/2);

        if abs(b - func_d) < abs(b + func_d)
            func_e = b + func_d;
        else
            func_e = b - func_d;
        endif

        h = -2 * feval(func, p2) / func_e;
        p = p2 + h;

        if abs(h) < tol
            sol = 1;
            break;
        endif

        p0 = p1;
        p1 = p2;
        p2 = p;
        h1 = p1 - p0;
        h2 = p2 - p1;
        d1 = (feval(func, p1) - feval(func, p0)) / h1;
        d2 = (feval(func, p2) - feval(func, p1)) / h2;
        d = (d1 - d2) / (h2 + h1);

        if proc
            printf("\n\n--------Iteración N° %d", n - 2);
            printf("\n\tp0 = %d", p0)
            printf("\n\tp1 = %d", p1)
            printf("\n\tp2 = %d", p2)
            printf("\n\tError = %d", abs(h))
            printf("\n\td = %d", d) 
        end

        n++;

    endwhile

    if n > numMaxIter
        warning(["\nMuller falla despues de " num2str(n) " iteraciones\n"]);
    end

    c = p;
    error = abs(h);
    numIter = n;

    if proc
        printf("\n\nSolución: %d\n\n", p)
    end

endfunction
