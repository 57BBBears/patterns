from implementation.controller import DeviceController
from implementation.devices import Barometer, Monitor, Thermometer, Voltmeter
from interfaces.mediator import Controller


def set_devices(controller_: Controller):
    return [
        Thermometer(controller_),
        Barometer(controller_),
        Voltmeter(controller_),
    ]


if __name__ == "__main__":
    controller = DeviceController()
    # test singleton
    assert controller is DeviceController()
    devices = set_devices(controller)
    monitor = Monitor(controller)
    verbose_monitor = Monitor(controller, "Monitoring devices...")
    controller.add(monitor).add(verbose_monitor)
    # measure and get info by monitors
    for device in devices:
        device.measure()
        verbose_monitor.measure()
        monitor.measure()
