from implementation.cranes import ShipCrane, TruckCrane
from implementation.vehicles import Ship, Truck


class RiverPort:
    @staticmethod
    def get_vehicle() -> Ship:
        return Ship()

    @staticmethod
    def get_crane() -> ShipCrane:
        return ShipCrane()


class RoadPort:
    @staticmethod
    def get_vehicle() -> Truck:
        return Truck()

    @staticmethod
    def get_crane() -> TruckCrane:
        return TruckCrane()
