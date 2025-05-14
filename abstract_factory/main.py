# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from core.port import Port
from implementation.ports import RoadPort, RiverPort


def main(port: Port):
    vehicle = port.get_vehicle()
    crane = port.get_crane()

    print(crane.handle(vehicle))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Road port")
    road_port = RoadPort()
    main(road_port)

    print("River port")
    river_port = RiverPort()
    main(river_port)
