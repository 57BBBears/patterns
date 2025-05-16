from interfaces.parcel import Parcel, ParcelVisitor


class Letter(Parcel):
    def accept(self, visitor: ParcelVisitor):
        visitor.visit_letter(self)

    @property
    def volume(self) -> int:
        return 0


class Box(Parcel):
    def __init__(self, *, length: int, width: int, height: int):
        self.length = length
        self.width = width
        self.height = height

    def accept(self, visitor: ParcelVisitor):
        visitor.visit_box(self)

    @property
    def volume(self) -> int:
        return self.length * self.width * self.height
