function [fxi] = LagrangeEstimacion(xi, x, y)
    %
    long = length(x);

    for i = 1:long

        # Determinacion de los numeradores
        numerador(i) = 1;

        for j = 1:long

            if i ~= j
                numerador(i) = numerador(i) * (xi - x(j));
            endif

            endfor;
            # Determinacion de los denominadores
            denominador = 1;

            for j = 1:long

                if i ~= j
                    denominador = denominador * (x(j) - x(i));
                endif

                endfor;

                # Division de los operandos
                termino(i) = numerador(i) / denominador;
                # Muestra por pantalla de la multiplicacion a realizar: yi * xi
                disp(["\t" num2str(termino(i)) " * " num2str(y(i)) " = " num2str(termino(i) * y(i))]);
                # Multiplicacion
                termino(i) = termino(i) * y(i);

                endfor;

                #Suma de coeficientes;
                fxi = sum(termino);
            endfunction
