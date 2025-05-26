from implementation.dtos import BaseDTO


class PrototypeRepository:
    """Contains available prototypes and
    allows to get them by name or by other attributes."""

    def __init__(self):
        self._prototypes: dict[str, BaseDTO] = {}

    def add(self, name: str, prototype: BaseDTO):
        self._prototypes[name] = prototype

    def remove(self, name: str):
        self._prototypes.pop(name, None)

    def __getitem__(self, item: str) -> BaseDTO:
        return self._prototypes[item].clone()

    def get_true(self) -> list[BaseDTO]:
        return [
            proto.clone()
            for proto in self._prototypes.values()
            if getattr(proto, "is_true", None)
        ]

    def get_by_color(self, color: str) -> list[BaseDTO]:
        return [
            proto.clone()
            for proto in self._prototypes.values()
            if getattr(proto, "color", None) == color
        ]
