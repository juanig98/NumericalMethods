function GE = GaussElim(A, B, proc = false)
    % A: Matriz de coeficientes
    % B: Vector de terminos independientes
    % Amp: Matriz ampliada
    % X: Vector de resultados

    if proc
        disp('Matrices:');
        disp('A =');
        disp(A)
        disp('b =');
        disp(B)
    end

    bb = length(B);
    n = length(A);

    if n ~= bb
        disp('Error: puede que la matriz de coeficientes no sea cuadrada, o falen datos al vector de terminos independientes')
    end

    if det(A) == 0
        disp('Error: La matriz es singular, su determinante es igual a cero')
        det(A) = 0
    end

    m = n + 1;
    Amp = [A B];
    p = 0;

    for i = 2:n
        k = i - 1;

        % Ordenamiento y pivoteo
        [a b] = max(abs(Amp(k:n, k)));
        b = b + p;
        fp = Amp(b, :);
        Amp(b, :) = Amp(k, :);
        Amp(k, :) = fp;

        if proc && b != k
            disp(["PERMUTACION: Se permuta la linea " num2str(b) ' por la linea ' num2str(k)]);
        end

        Amp

        % Etapa hacia adelante (Eliminacion)
        for j = i:n
            r = Amp(j, k) / Amp(k, k);

            if proc
                disp(["ELIMINACION: L" num2str(j) ' - L' num2str(k) ' x ' num2str(r)]);
            end

            for l = 1:m
                Amp(j, l) = Amp(j, l) - r * Amp(k, l);
            end

        end

        p = p + 1;

        if proc
            Amp
        end

    end

    %Muestra la matriz despues de la eliminaci?n
    if proc
        disp('Matriz triangular (despues de la eliminacion)')
        Amp
    end

    % Etapa hacia atras (calculo de incognitas)
    X = zeros(n, 1);

    for i = n:-1:1

        for j = n:-1:1
            Amp(i, m) = Amp(i, m) - Amp(i, j) * X(j);
        end

        X(i) = Amp(i, m) / Amp(i, i);
    end

    EA = X;

    if proc
        disp('Vector de resultados')
        EA
    end

end
