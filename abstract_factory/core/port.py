from typing import Protocol

from core.crane import Crane
from core.vehicle import Vehicle


class Port(Protocol):
    def get_vehicle(self) -> Vehicle:
        ...

    def get_crane(self) -> Crane:
        ...
