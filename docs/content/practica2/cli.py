from models.parking import ParkingLot, ParkingSpot, VehicleType, Car, Motorcycle, HourlyRatePolicy

def main():
    # Inicialización del sistema
    spots = [ParkingSpot(f"A{i}", VehicleType.CAR) for i in range(1, 4)] + \
            [ParkingSpot(f"M{i}", VehicleType.MOTORCYCLE) for i in range(1, 3)]
    
    parking = ParkingLot(spots, HourlyRatePolicy())

    while True:
        print("\n--- SISTEMA DE ESTACIONAMIENTO (CLI) ---")
        print("1. Entrada | 2. Salida | 3. Ver Estado | 4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            placa = input("Ingrese placa: ")
            tipo = input("Tipo (1: Carro / 2: Moto): ")
            v = Car(placa) if tipo == "1" else Motorcycle(placa)
            
            ticket = parking.enter_vehicle(v)
            if ticket:
                print(f"¡Éxito! Ticket #{ticket['id']} asignado en {ticket['s'].spot_id}")
            else:
                print("Error: No hay espacios disponibles.")

        elif opcion == "2":
            try:
                tid = int(input("ID del Ticket a retirar: "))
                costo = parking.exit_vehicle(tid)
                if costo is not None:
                    print(f"Vehículo retirado. Total a cobrar: ${costo}")
                else:
                    print("Error: Ticket no encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcion == "3":
            status = parking.get_status()
            print(f"Ocupación: {status['occupied']}/{status['total']}")
            print("Tickets activos:", [t['id'] for t in status['tickets']])

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

if __name__ == "__main__":
    main()