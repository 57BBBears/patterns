from interfaces.connector import Connector, ConnectorError


class Entity:
    connector: Connector

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password
        self.data: dict = {}

    def _get_connector(self) -> Connector:
        try:
            return self.connector
        except AttributeError as e:
            raise ConnectorEntityError from e

    def get_data(self):
        con = self._get_connector()
        try:
            con.connect(self.login, self.password)
            self.data = con.get_data()
        except ConnectorError:
            ...
        finally:
            con.disconnect()


class VerboseEntity(Entity):
    def __str__(self) -> str:
        return f"Entity with data: {self.data}"


class EntityError(Exception): ...


class ConnectorEntityError(Exception):
    def __init__(self, message: str = "Connector is not set."):
        super().__init__(message)
