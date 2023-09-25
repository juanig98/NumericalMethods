function Ja = Jacobi(A, B, e, n)
    % A Matriz de terminos de coeficientes
    % B vector de terminos independientes
    % e Error tolerable
    % n N?mero m?ximo de iteraciones
    f = length(A);
    bb = length(B)
    cont = 0;
    X = zeros(f, 1);
    Xk = zeros(f, 1);
    Xant = zeros(f, 1);
    wcorto = 0; %% se usa para saber si corta por minimo de tolerancia, es una bandera

    if f ~= bb
        disp('Error: puede que la matriz de coeficientes no sea cuadrada, o falten datos al vector de terminos independientes')
        return
    end

    if det(A) == 0
        disp('Error: La matriz es singular, su determinante es igual a cero')
        det(A) == 0
        return
    end

    for t = 1:n
        printf("\n\n--- Iteración %d ---\n", t)

        for i = 1:f
            d = 0;

            for j = 1:f

                if j ~= i
                    d = d + A(i, j) * Xk(j);
                end

            end

            %	Xk(i)=X(i);
            X(i) = (B(i) - d) / A(i, i);
        end

        err = norm(X - Xk, inf) / norm(X, inf);
        n = ['Error ', num2str(err), '. Iteracion  ', num2str(t)];

        if bb == 3
            printf("x1 = %d,  x2 = %d, x3 = %d \nError: %d", X, err)
        end

        if bb == 4
            printf("x1 = %d,  x2 = %d, x3 = %d, x4 = %d \nError: %d", X, err)
        end

        if err <= e
            wcorto = 1;
            break
        end

        Xk = X;
    end

    if wcorto == 1
        printf('\n\nSALIDA POR ERROR\n');
    else
        printf('\n\nSALIDA POR ITERACCIONES MÁXIMAS\n');
    end

    disp(n);
    disp(X);
    Ja = X;
end
