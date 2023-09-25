% MÉTODO DE GAUSS JORDAN
% Este método difiere con el método de eliminación gaussiana puesto que cuando se elimina
% una incógnica no sólo se elimina de las ecuaciones siguientes sino de todas las otras
% ecuaciones. De esta forma el paso de eliminación genera una matriz identidad en lugar
% de una matriz triangular. Por consiguiente no es ncesario emplear la sustitución hacía
% atrás para obtener la solución.

function GJ = GaussJordan(A, B, proc = false)
    # A: Matriz de coeficientes
    # B: Vector de términos independientes

    n = length(A);
    m = n + 1;
    Amp = [A B];

    if proc
        printf("\nMatriz inicial:\n\n");
        disp(Amp);
        printf("\n");
    end

    for i = 1:n
        pivot = i;

        if proc
            printf("---------------------------------------- Paso %d ----------------------------------------\n", i);
        end

        for j = i + 1:n

            if abs(Amp(j, i)) > abs(Amp(pivot, i))
                pivot = j;
            end

        end

        if pivot != i && proc
            printf("- Se reemplaza F%d por F%d\n", i, pivot);
        end

        Amp([i, pivot], :) = Amp([pivot, i], :);

        pivot = Amp(i, i);
        Amp(i, :) = Amp(i, :) / pivot;

        if proc
            printf("- Se divide la F%d por %f (pivot)\n\nMatriz:\n\n", i, pivot);
            disp(Amp);
            printf("\n")
        end

        for j = 1:n

            if j != i
                fact = Amp(j, i);
                Amp(j, :) = Amp(j, :) - fact * Amp(i, :);

                if proc
                    printf("- Se resta la F%d por la F%d multiplicado por %f\n\n", j, i, fact);
                end

            end

        end

        if proc
            printf("\nMatriz resultante del paso %d:\n", i);
            disp(Amp);  
            printf("\n")
        end

    end

    result = Amp(:, n + 1);
end
