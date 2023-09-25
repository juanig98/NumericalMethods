function R = EulerMejorado(f, a, b, y0, h, proc = false)
    % Aproxima el ivp "f", en "b" a partir de "a" con valor inicial "y0" y "M" pasos
    % con el M todo de Euler.
    % Salida:
    % Vector de dimension M+1x2, que contiene el valor de la variable
    % independiente en la primer componente y el valor de la funcion
    % en dicho punto.
    % Entrada:
    % - f : La funcion en formato estandart f(t, y(t))
    % - a : ordenada inicial
    % - b : ordenada final
    % - y0: valor de la funcion en a.
    % - M : cantidad de pasos.
    format long;
    M = (b - a) / h; %Tama o del paso.
    T = zeros(1, M + 1);
    Y = zeros(1, M + 1);
    T = a:h:b;
    Y(1) = y0;

    if proc
        printf("\nInicio:")
        printf("\nt = 0\t\ty = %d", Y(1))
    endif

    ref4 = y0;

    for k = 1:M
        kk = k + 1;

        % Y(kk) = Y(k) + h * feval(f, Y(k), T(k));
        Y(kk) = ref4 + h * feval(f, ref4);
        ref1 = ref4 + (feval(f, ref4) + feval(f, Y(kk))) / 2 * h;
        ref2 = ref4 + (feval(f, ref4) + feval(f, ref1)) / 2 * h;
        ref3 = ref4 + (feval(f, ref4) + feval(f, ref2)) / 2 * h;
        ref4 = ref4 + (feval(f, ref4) + feval(f, ref3)) / 2 * h;


        if proc
            printf("\n\nt = %d\t y = %d", T(kk), Y(kk))
            printf("\n-> ref1 = %d ref2 = %d ref3 = %d ref4 = %d", ref1, ref2, ref3, ref4);
        endif

    endfor

    if proc
        printf("\n\nValor final: %d\n", Y(kk))
        printf("\n")
    endif

    R = [Y'];
endfunction
