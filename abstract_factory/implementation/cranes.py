from core.vehicle import Vehicle


class ShipCrane:
    def handle(self, vehicle: Vehicle) -> str:
        return f"Корабль " + vehicle.move() + ", поэтому разгружаю с воды."


class TruckCrane:
    def handle(self, vehicle: Vehicle) -> str:
        return f"Грузовик " + vehicle.move() + ", поэтому разгружаю с дороги."
