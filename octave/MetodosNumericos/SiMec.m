function SiMec(m, k, am, h, ts, filename = false)
    % m Peso del cuerpo
    % k Fuerza Resorte
    % am Fuerza Amortiguador
    % h Tamaño de paso
    % ts Tiempo de la simulación

    printf('Simulación del sistema mecánico (Resorte-Amortiguador)')
    printf('---------------------------------------')
    A = k;
    B = am;
    T(1) = 0;
    P = m; % Peso del cuerpo
    M = P / 9.8; % Inercia
    d = ts; % Duracion de la simulacion
    dpos = 0; % Desplazamiento maximo
    dneg = 0; % Desplazamiento minimo
    tdpos = 0; % Tiempo desplazamiento maximo
    tvpos = 0; % Tiempo velocidad maxima
    vpos = 0; % Velocidad maxima
    vneg = 0; % Velocidad negativa
    tdneg = 0; % Momento desplazamiento minimo
    tvneg = 0; % Momento velocidad minima
    x1 = 0; % Desplazamiento inicial
    x2 = 0; % Velocidad inicial

    f = inline('x2', 't', 'x1', 'x2');
    g = inline('co1-co2*x2-co3*x1', 't', 'x1', 'x2', 'co1', 'co2', 'co3');
    ls = d / h;
    Y(:, 1) = [x1; x2];
    wti = 0;

    if !filename
        filename = datestr(date, 0) 
    end

    fid = fopen(['./tmp/', filename, '.txt'], 'w');

    for t = 0:ls

        if t < 20
            co1 = 5 * 9.8 / P;
        else
            co1 = 0;
        end

        co2 = (B * 9.8 / P);
        co3 = (A * 9.8 / P);

        k11 = h * f(t, x1, x2);
        k21 = h * g(t, x1, x2, co1, co2, co3);

        k12 = h * f(t + h * .5, x1 + k11 / 2, x2 + k21 * 0.5);
        k22 = h * g(t + h * .5, x1 + k11 / 2, x2 + k21 * 0.5, co1, co2, co3);

        k13 = h * f(t + h * .5, x1 + k12 / 2, x2 + k22 * 0.5);
        k23 = h * g(t + h * .5, x1 + k12 / 2, x2 + k22 * 0.5, co1, co2, co3);

        k14 = h * f(t + h, x1 + k13, x2 + k23);
        k24 = h * g(t + h, x1 + k13, x2 + k23, co1, co2, co3);

        x1 = x1 + (k11 + 2 * k12 + 2 * k13 + k14) / 6;
        x2 = x2 + (k21 + 2 * k22 + 2 * k23 + k24) / 6;

        if mod(t, 10) == 0
            fprintf(fid, '%f\t%f\t%f\n', t, x1, x2);

            wti = wti + 1;
            Y(1, wti + 1) = x1;
            Y(2, wti + 1) = x2;
            T(wti + 1) = wti;
        end

        if x1 > dpos
            dpos = x1;
            tdpos = t / 10;
        end

        %%%% Desplazamiento Negativo
        if x1 < dneg
            dneg = x1;
            tdneg = t / 10;
        end

        %%%  Velocidad Positiva
        if x2 > vpos
            vpos = x2;
            tvpos = t / 10;
        end

        %%%  Velocidad Negativa
        if x2 < vneg
            vneg = x2;
            tvneg = t / 10;
        end

    end

    fclose(fid);

    % Presentacion de los resultados
    printf('\n\nRESULTADOS');
    printf('\n\nDesplazamiento maximo: %3.4f metros', dpos);
    printf('\nProducido a los: %3.1f segundos', tdpos);
    printf('\n\nDesplazamiento minimo: %3.4f metros', dneg);
    printf('\nProducido a los: %3.1f segundos', tdneg);
    printf('\n\nVelocidad maxima: %3.4f m/s', vpos);
    printf('\nProducida a los: %3.1f segundos', tvpos);
    printf('\n\nVelocidad minima: %3.4f m/s', vneg);
    printf('\nProducida a los: %3.1f segundos', tvneg);

    % Graficacion de resultados
    plot(T, Y(1, :), '-', T, Y(2, :), ':');
    xlabel('Tiempo en segundos');
    ylabel('Desplazamiento y Velocidad')
    axis('auto');
    fprintf('\n');
endfunction
