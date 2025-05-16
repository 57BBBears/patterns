from abc import ABC, abstractmethod


class Parcel(ABC):
    @abstractmethod
    def accept(self, visitor: "ParcelVisitor"): ...

    @property
    @abstractmethod
    def volume(self) -> int: ...


class ParcelVisitor(ABC):
    @abstractmethod
    def visit_letter(self, letter: Parcel): ...

    @abstractmethod
    def visit_box(self, box: Parcel): ...
