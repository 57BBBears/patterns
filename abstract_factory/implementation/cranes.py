from core.vehicle import Vehicle


class ShipCrane:
    def handle(self, vehicle: Vehicle) -> str:
        return f"A ship " + vehicle.move() + ", so unloading from the water."


class TruckCrane:
    def handle(self, vehicle: Vehicle) -> str:
        return f"A truck " + vehicle.move() + ", so unloading from the road."
