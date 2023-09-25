function [C, L] = Lagrange (X, Y)

    % Entrada  - X es un vector que contiene una lista de las abscisas
    %          - Y es un vector que contiene una lista de las ordenadas
    % Salida   - C es una matriz que contiene los coeficientes del
    %            polinomio interpolante de Lagrange
    %          - L es una matriz que contiene los coeficientes de los
    %            polinomios de Lagrange

    %  METODOS NUMERICOS: Programas en Matlab
    % (c) 2004 por John H. Mathews y Kurtis D. Fink
    %  Software complementario acompa�ando al texto:
    %  METODOS NUMERICOS con Matlab, Cuarta Edicion
    %  ISBN: 0-13-065248-2
    %  Prentice-Hall Pub. Inc.
    %  One Lake Street
    %  Upper Saddle River, NJ 07458

    w = length(X);
    n = w - 1;
    L = zeros(w, w);

    % Formar los polinomios coeficientes de Lagrange

    for k = 1:n + 1
        V = 1;

        for j = 1:n + 1

            if k ~= j
                V = conv(V, poly(X(j))) / (X(k) - X(j));
            end

        end

        L(k, :) = V;
    end

    disp(["x = " num2str(X)]);
    disp(["y = " num2str(Y)]);

    disp("\nP(x) = ");
    disp(L);
    % Determinar los coeficientes del polinomio interpolador de Lagrange

    C = Y * L;
