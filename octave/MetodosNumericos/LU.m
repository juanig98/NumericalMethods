function LU = LoUp(A, B)
    % A: Matriz de coeficientes
    % B: Vector de terminos independientes
    % Amp: Matriz que toma los valores de la matriz A luego se descompone en U
    % L: Matriz L
    % Z: Vector Z
    % X: Vector de resultados

    bb = length(B);
    n = length(A);

    if n ~= bb
        disp('Error: puede que la matriz de coeficientes no sea cuadrada, \n o falen datos al vector de terminos independientes')
    elseif det(A) == 0
        disp('Error: La matriz es singular, su determinante es igual a cero')
        det(A) == 0

    else
        [L, U, P] = lu(A);

        B = P * B;
        # Muestra las matrices L y U
        printf('Matriz L\n')
        disp(L)
        printf('\nMatriz U\n')
        disp(U)
        printf('\n')

        # Calculo del vector Z (L*Z=B)
        Z = zeros(n, 1);

        for i = 1:n
            m = i - 1;

            for j = 1:m
                Z(i) = Z(i) + L(i, j) * Z(j);
            end

            Z(i) = B(i) - Z(i);
        end

        disp('Vector')
        disp(Z)

        % Calculo de resultados U*z=X
        X = zeros(n, 1);

        for i = n:-1:1

            for j = n:-1:1
                Z(i) = Z(i) - U(i, j) * X(j);
            end

            X(i) = Z(i) / U(i, i);

        end

        LU = X;
        printf('\nResultado:\n')
        disp(LU)

    end

end
