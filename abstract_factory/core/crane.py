from typing import Protocol

from core.vehicle import Vehicle


class Crane(Protocol):
    def handle(self, vehicle: Vehicle) -> str:
        ...
