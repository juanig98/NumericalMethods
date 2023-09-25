function [sol, numIter, error, c] = Biseccion(func, a, b, err, maxIter, proc = false, sol = false)
    % Esta funcion genera una aproximacion de la raiz c de la
    %   funcion derivable f(x) en el intervalo [a,b] mediante el metodo de Biseccion.
    % Datos necesarios para llamar a la funcion:
    %   func, expresion de f(x);
    %   a, valor inicial del intervalo;
    %   b, valor final del intervalo;
    %   err, tolerancia maxima de error;
    %   maxIter, numero maximo de iteraciones;
    %   proc, (0 si no se desea mostrar el proceso de aproximacion, 1 si se desea ver el proceso de aproximacion)
    % La funcion devuelve como respuesta tres valores:
    %      c = valor aproximado de la rai�z;
    %      err = |f(c)|;
    %      numiter = numero de iteraciones realizadas.
    %      sol = (1 si existe raiz en [a,b], 0 si no existe raiz en el intervalo [a,b] por los criterios buscados
    sol = 0;
    fa = feval(func, a);
    fb = feval(func, b);
    c = (a + b) / 2;
    fc = feval(func, c);
    error = abs(a - b);
    n = 1;

    while err < error && n < maxIter;
        c = (a + b) / 2;
        fc = feval(func, c);

        if proc
            printf("\n--------- Iteracion N° %d\n", n);
            printf("a = %d\t f(a) = %d\n", a, fa);
            printf("b = %d\t f(b) = %d\n", b, fb);
            printf("c = %d\t f(c) = %d\n", c, fc);
            printf("\nError = %d\n\n", error);
        endif

        if fb * fc > 0; % La raiz esta en [a,c]
            b = c;
            fb = fc;
        else fb * fc < 0; % La raiz esta en [c,b]
            a = c;
            fa = fc;
        end

        n++; % Contador de iteraciones
        error = abs(a - b);
    end

    if n >= maxIter
        printf("\nSALIDA POR ITERACIONES MÁXIMAS\n");
    elseif c == 0
        printf("\nSALIDA POR SOLUCIÓN ENCONTRADA\n");
        sol = 1;
    elseif err > error;
        printf("\nSALIDA POR ERROR MÍNIMO\n");
    endif

    if sol || proc
        printf("\nSolución: %d\n\n", c);
    end

    numIter = n;
endfunction
