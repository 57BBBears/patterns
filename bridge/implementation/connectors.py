from interfaces.connector import Connector


class DummyConnector(Connector):
    def connect(self, login: str, password: str):
        print(f"Connected {self.__class__} with {login}:{password}")

    def connect_count(self) -> int:
        return 0

    def disconnect(self):
        print(f"Disconnected {self.__class__}")

    def get_data(self) -> dict:
        return {"data": "dummy"}


class QueueConnector(Connector):
    def __init__(self):
        self._logins: list[str] = []

    def connect(self, login: str, password: str):
        print(f"Connected {self.__class__} with {login}:{password}")
        self._logins.append(login)

    def connect_count(self) -> int:
        return len(self._logins)

    def disconnect(self):
        print(f"Disconnected {self.__class__}")

    def get_data(self) -> dict:
        return {"data": self.connect_count()}
