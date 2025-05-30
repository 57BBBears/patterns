from typing import Literal

from implementation.devices import Barometer, Monitor, Thermometer, Voltmeter
from interfaces.mediator import Controller, Device


class DeviceController(Controller):
    """Gets measurements from devices and set monitor values depending on the gotten
    values and own limits, thus a controller manages collaboration."""

    _instance = None

    PRESSURE_LIMIT = 80
    TEMP_LIMIT = 0
    VOLTAGE_LIMIT = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        self._devices = []

    def add(self, device: Device):
        self._devices.append(device)

        return self

    def remove(self, device: Device):
        try:
            self._devices.remove(device)

            return self

        except ValueError:
            ...

    def get_measurement(self, device: Device):
        """Handle a device by its type."""
        if isinstance(device, Thermometer):
            self._handle_temperature(device.value)
        if isinstance(device, Barometer):
            self._handle_pressure(device.value)
        if isinstance(device, Voltmeter):
            self._handle_voltage(device.value)

    def _handle_temperature(self, value: float | None):
        self._inform_monitors(value, ">", self.TEMP_LIMIT)

    def _handle_pressure(self, value: float | None):
        self._inform_monitors(value, "<", self.PRESSURE_LIMIT)

    def _handle_voltage(self, value: float | None):
        self._inform_monitors(value, "!=", self.VOLTAGE_LIMIT)

    def _inform_monitors(
        self,
        value: float | None,
        if_stmt: Literal[">", "<", "==", "!="],
        criteria: float,
    ):
        for device in self._devices:
            if isinstance(device, Monitor):
                device._value = 1 if self._is_value_ok(value, if_stmt, criteria) else 0

    @staticmethod
    def _is_value_ok(
        value: float | None, if_stmt: Literal[">", "<", "==", "!="], criteria: float
    ) -> bool:
        if value is None:
            return False

        match if_stmt:
            case ">":
                return value > criteria
            case "<":
                return value < criteria
            case "==":
                return value == criteria
            case "!=":
                return value != criteria
            case _:
                raise False
