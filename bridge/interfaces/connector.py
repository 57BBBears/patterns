from abc import ABC, abstractmethod


class Connector(ABC):
    @abstractmethod
    def connect(self, login: str, password: str): ...

    @abstractmethod
    def connect_count(self) -> int: ...

    @abstractmethod
    def disconnect(self): ...

    @abstractmethod
    def get_data(self) -> dict: ...


class ConnectorError(Exception): ...
