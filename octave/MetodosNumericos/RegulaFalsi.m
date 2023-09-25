function [sol, numIter, error, c] = RegulaFalsi(func, a, b, tol, numIter, proc = false, verSol = false)
    % Esta funcion genera una aproximacion de la raiz c de la
    %   funcion derivable f(x) en el intervalo [a,b] mediante el metodo Regula-Falsi.
    % Datos necesarios para llamar a la funcion:
    %   func, expresion de f(x);
    %   a, valor inicial del intervalo;
    %   b, valor final del intervalo;
    %   tol, tolerancia maxima de error;
    %   numIter, numero maximo de iteraciones;
    %   proc, (0 si no se desea mostrar el proceso de aproximacion, 1 si se desea ver el proceso de aproximacion)
    % La funcion devuelve como respuesta tres valores:
    %      c = valor aproximado de la rai�z;
    %      err = |f(c)|;
    %      numiter = numero de iteraciones realizadas.
    %      sol = (1 si existe raiz en [a,b], 0 si no existe raiz en el intervalo [a,b] por los criterios buscados
    n = 1;
    sol = 0;
    ao = a;
    bo = b;
    v_sol = verSol;

    if proc
        v_sol = true;
    end

    func_a = feval(func, a);
    func_b = feval(func, b);

    while n <= numIter
        c = b - func_b * (b - a) / (func_b - func_a);
        error = abs(c - b);

        if proc
            printf("\n\n---------Iteracion N° %d  \n", n);
            printf("a = %d\t\t f(a) = %d\n", a, feval(func, a));
            printf("b = %d\t\t f(b) = %d\n", b, feval(func, b));
            printf("c = %d\t\t f(c) = %d\n", c, feval(func, c));
            printf("\nError = %d", error);
        endif

        if error < tol
            sol = 1;
            break;
        else
            n++;
            func_c = feval(func, c);

            if c < ao || c > bo
                v_sol = false;
                break;
            end

            if func_c * func_b < 0
                a = b;
                func_a = func_b;
            end

            b = c;
            func_b = func_c;
        end

    endwhile

    if n > numIter
        printf("\nSALIDA POR ITERACCIONES MÁXIMAS ");
        return
    endif

    if v_sol 
        printf("\n\nSolución: %d\n\n", c)
    end

    numIter = n;
endfunction
