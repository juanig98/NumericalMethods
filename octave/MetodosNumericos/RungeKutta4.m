function R = RungeKutta4 (f, a, b, y0, h, proc = false)

    % Entrada   - f es la funcion introducida como cadena de caracteres  'f'
    %           - a y b son los extremos izquierdo y derecho
    %           - y0 es la condicion inicial  y(a)
    %           - M es el numero de pasos
    % Salida    - R = [T', Y'] donde  T  es el vector de abscisas
    %             y  Y  es el vector de ordenadas

    M = (b - a) / h;
    T = zeros(1, M + 2);
    Y = zeros(1, M + 1);
    T = a:h:b;
    Y(1) = y0;

    for j = 1:M
        k1 = h * feval(f, Y(j), T(j));
        k2 = h * feval(f, Y(j) + k1 / 2, T(j) + h / 2);
        k3 = h * feval(f, Y(j) + k2 / 2, T(j) + h / 2);
        k4 = h * feval(f, Y(j) + k3, T(j) + h);

        if proc
            printf("\n\n---Iteración N° %d", j)
            printf("\nt = %d", T(j))
            printf("\ny = %d", Y(j))
            printf("\nk1 = %d", k1)
            printf("\nk2 = %d", k2)
            printf("\nk3 = %d", k3)
            printf("\nk4 = %d", k4)
        endif

        Y(j + 1) = Y(j) + (k1 + 2 * k2 + 2 * k3 + k4) / 6;
    end

    R = [T', Y'];

    if proc
        printf("\n\nSolución\n")
        disp(R)
    endif

endfunction
