from random import randint

from interfaces.mediator import Controller, Device


class Thermometer(Device):
    def _get_value(self):
        self._value = randint(-10, 10)
        print(f"Checking temperature... {self._value}")


class Barometer(Device):
    def _get_value(self):
        self._value = randint(0, 100)
        print(f"Checking pressure... {self._value}")


class Voltmeter(Device):
    def _get_value(self):
        self._value = randint(0, 10)
        print(f"Checking voltage... {self._value}")


class Monitor(Device):
    def __init__(self, controller: Controller, message: str = ""):
        self._message = message
        super().__init__(controller)

    def _get_value(self):
        print(self._message) if self._message else ...
        print("Ok") if self._value else print("Not Ok")
