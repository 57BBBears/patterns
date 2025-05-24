from typing import Protocol


class CloneProto(Protocol):
    def clone(self): ...
