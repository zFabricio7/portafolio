% ----- REPRESENTACIÓN DEL ENTORNO -----
% Formato:
% escenario(PosicionMono, EstadoMono, PosicionCaja, Banana)
%
% PosicionMono y PosicionCaja:
% puerta, ventana, centro
%
% EstadoMono:
% piso, arriba_caja
%
% Banana:
% sin_banana, con_banana

% ----- ACCIONES POSIBLES -----

% Acción: agarrar la banana
accion(escenario(centro, arriba_caja, centro, sin_banana),
       agarrar,
       escenario(centro, arriba_caja, centro, con_banana)).

% Acción: subir a la caja
accion(escenario(Lugar, piso, Lugar, EstadoBanana),
       subir_caja,
       escenario(Lugar, arriba_caja, Lugar, EstadoBanana)).

% Acción: mover la caja
accion(escenario(Inicio, piso, Inicio, EstadoBanana),
       mover_caja(Inicio, Destino),
       escenario(Destino, piso, Destino, EstadoBanana)) :-
    Inicio \== Destino.

% Acción: desplazarse
accion(escenario(Inicio, piso, PosCaja, EstadoBanana),
       desplazarse(Inicio, Destino),
       escenario(Destino, piso, PosCaja, EstadoBanana)) :-
    Inicio \== Destino.

% ----- BÚSQUEDA DE SOLUCIÓN -----

% Caso final
resolver(escenario(_, _, _, con_banana), []).

% Caso recursivo
resolver(EstadoActual, [Paso | PasosRestantes]) :-
    accion(EstadoActual, Paso, NuevoEstado),
    resolver(NuevoEstado, PasosRestantes).