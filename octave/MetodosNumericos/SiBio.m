function SiBio(ut, t0, tf, x0, y0, r, s, a, b)
    % ut Número de iteraciones.
    % t0 Tiempo inicial
    % tf Tiempo final
    % r Coeficiente de la razón de crecimiento de presas P.
    % s Coeficiente de la razón de muerte de depredador D.
    % a Constante de proporcionalidad que mide el número de interacciones presa-depredador en la que la presa es devorada.
    % b Constante de proporcionalidad que mide el beneficio a la población de depredadores D de una presa P devorada.

    R(1) = x0; % Condición inicial. Población de liebres/conejos
    F(1) = y0; % Condición inicial. Ponlación de linces/zorros

    h = (tf - t0) / ut; % Espacio entre iteraciones sucesivas.

    R_Max = 0;
    R_Min = 999999;
    F_Max = 0;
    F_Min = 999999;

    for i = 1:ut

        % Cálculo de las constantes k1,k2,k3,k4.
        k1 = [r * R(i) - a * F(i) * R(i), -s * F(i) + b * F(i) * R(i)];
        k2 = [r * (R(i) + h * k1(1) / 2) - a * (F(i) + h * k1(2) / 2) * (R(i) + h * k1(1) / 2), -s * (F(i) + h * k1(2) / 2) + b * (F(i) + h * k1(2) / 2) * (R(i) + h * k1(1) / 2)];
        k3 = [r * (R(i) + h * k2(1) / 2) - a * (F(i) + h * k2(2) / 2) * (R(i) + h * k2(1) / 2), -s * (F(i) + h * k2(2) / 2) + b * (F(i) + h * k2(2) / 2) * (R(i) + h * k2(1) / 2)];
        k4 = [r * (R(i) + h * k3(1)) - a * (F(i) + h * k3(2)) * (R(i) + h * k3(1)), -s * (F(i) + h * k3(2)) + b * (F(i) + h * k3(2)) * (R(i) + h * k3(1))];

        % Cálculo del próximo valor de R, F.
        R(i + 1) = R(i) + h * (k1(1) + 2 * k2(1) + 2 * k3(1) + k4(1)) / 6;
        F(i + 1) = F(i) + h * (k1(2) + 2 * k2(2) + 2 * k3(2) + k4(2)) / 6;

        if R(i + 1) > R_Max
            R_Max = R(i + 1);
            P_R_Max = i + 1;
        endif

        if R(i + 1) < R_Min
            R_Min = R(i + 1);
            P_R_Min = i + 1;
        endif

        if F(i + 1) > F_Max
            F_Max = F(i + 1);
            P_F_Max = i + 1;
        endif

        if F(i + 1) < F_Min
            F_Min = F(i + 1);
            P_F_Min = i + 1;
        endif

        endfor;

        T = t0:h:tf;

        % Gráficos

        hold on
        figure(1)% Grafico Y = población, X = Tiempo
        title("Poblacion-Tiempo simulación Presa-Predador")
        ylabel('Población');
        xlabel('Tiempo');

        plot(T, R, 'r', 'Color', 'blue')
        plot(T, F, 'g', 'Color', 'red')
        legend('Liebres/conejos', 'Linces/Zorros');

        figure(2)% Grafico de problaciones
        title("Grafico de poblaciones Presa-Predador")
        plot(R, F)

        hold off

        disp(["Máxima población de presas: " num2str(R_Max) ". En el periodo/ciclo: " num2str(P_R_Max)]);
        disp(["Mínima población de presas: " num2str(R_Min) ". En el periodo/ciclo: " num2str(P_R_Min)]);
        disp(["Máxima población de depredadores: " num2str(F_Max) ". En el periodo/ciclo: " num2str(P_F_Max)]);
        disp(["Mínima población de depredadores: " num2str(F_Min) ". En el periodo/ciclo: " num2str(P_F_Min)]);
    endfunction
