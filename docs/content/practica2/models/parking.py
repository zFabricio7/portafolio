from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional, Protocol

# Enumeraciones para tipos de vehículos y estados
class VehicleType(Enum):
    CAR = "CAR"
    MOTORCYCLE = "MOTORCYCLE"

# Clases de Dominio (Herencia y Subtipos)
@dataclass
class Vehicle:
    plate: str
    v_type: VehicleType

class Car(Vehicle):
    def __init__(self, plate: str):
        super().__init__(plate, VehicleType.CAR)

class Motorcycle(Vehicle):
    def __init__(self, plate: str):
        super().__init__(plate, VehicleType.MOTORCYCLE)

@dataclass
class ParkingSpot:
    spot_id: str
    allowed_type: VehicleType
    occupied: bool = False
    current_vehicle: Optional[Vehicle] = None

    def is_available_for(self, vehicle: Vehicle) -> bool:
        return not self.occupied and self.allowed_type == vehicle.v_type

    def park(self, vehicle: Vehicle):
        self.occupied = True
        self.current_vehicle = vehicle

    def release(self):
        self.occupied = False
        self.current_vehicle = None

# Polimorfismo mediante Protocolos (Interface de Cobro)
class RatePolicy(Protocol):
    def calculate(self, hours: float, vehicle: Vehicle) -> float: ...

class HourlyRatePolicy:
    def calculate(self, hours: float, vehicle: Vehicle) -> float:
        # Tarifa: Carro $20/hr, Moto $10/hr
        rate = 20.0 if vehicle.v_type == VehicleType.CAR else 10.0
        return round(max(1.0, hours) * rate, 2)

# Clase Principal (Encapsulación y Composición)
class ParkingLot:
    def __init__(self, spots: List[ParkingSpot], policy: RatePolicy):
        self._spots = spots
        self._active_tickets = {}
        self._policy = policy
        self._next_id = 1
        self.total_revenue = 0.0

    def enter_vehicle(self, vehicle: Vehicle):
        for spot in self._spots:
            if spot.is_available_for(vehicle):
                spot.park(vehicle)
                ticket = {
                    "id": self._next_id, 
                    "v": vehicle, 
                    "s": spot, 
                    "t": datetime.now()
                }
                self._active_tickets[self._next_id] = ticket
                self._next_id += 1
                return ticket
        return None

    def exit_vehicle(self, ticket_id: int):
        ticket = self._active_tickets.pop(ticket_id, None)
        if ticket:
            # Cálculo de tiempo (mínimo 1 hora)
            hours = (datetime.now() - ticket['t']).total_seconds() / 3600
            cost = self._policy.calculate(hours, ticket['v'])
            ticket['s'].release()
            self.total_revenue += cost
            return cost
        return None

    def get_status(self):
        return {
            "occupied": sum(1 for s in self._spots if s.occupied),
            "total": len(self._spots),
            "tickets": list(self._active_tickets.values())
        }