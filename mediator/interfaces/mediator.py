from abc import ABC, abstractmethod


class Controller(ABC):
    """Mediator to control collaboration between devices."""

    @abstractmethod
    def add(self, device: "Device") -> "Controller": ...

    @abstractmethod
    def remove(self, device: "Device") -> "Controller | None": ...

    @abstractmethod
    def get_measurement(self, device: "Device"): ...


class Device:
    """Base class for devices with a fabric method."""

    def __init__(self, controller: Controller):
        self._controller = controller
        self._value: float | None = None

    def measure(self):
        self._get_value()
        self._controller.get_measurement(self)

    @abstractmethod
    def _get_value(self): ...

    @property
    def value(self):
        return self._value
