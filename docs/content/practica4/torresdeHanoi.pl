% Caso base:
% Cuando solamente queda un disco
torres_hanoi(1, Inicio, Final, _, _) :-
    mostrar_paso(Inicio, Final).

% Caso recursivo
torres_hanoi(Cantidad, Inicio, Final, Auxiliar, Contador) :-
    Cantidad > 1,
    Temporal is Cantidad - 1,

    % Mover discos al auxiliar
    torres_hanoi(Temporal, Inicio, Auxiliar, Final, Contador),

    % Mover disco principal
    mostrar_paso(Inicio, Final),

    % Mover discos al destino
    torres_hanoi(Temporal, Auxiliar, Final, Inicio, Contador).

% Mostrar movimiento
mostrar_paso(Inicio, Final) :-
    write('Mover disco desde '),
    write(Inicio),
    write(' hacia '),
    write(Final),
    nl.

% Predicado principal
iniciar_hanoi(Cantidad) :-
    write('Resolución de Torres de Hanoi con '),
    write(Cantidad),
    write(' discos'),
    nl,

    torres_hanoi(Cantidad, 'A', 'C', 'B', _).