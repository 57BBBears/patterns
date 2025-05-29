from typing import Any, Protocol


class Command(Protocol):
    def execute(self) -> Any: ...
