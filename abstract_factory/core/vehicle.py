from typing import Protocol


class Vehicle(Protocol):
    def move(self) -> str:
        ...
