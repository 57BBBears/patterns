from dataclasses import dataclass

from implementation.mixins import CloneMixin


@dataclass
class BaseDTO(CloneMixin):
    """Just a simple Data Transfer Object."""

    name: str
    value: int


@dataclass
class ColoredDTO(BaseDTO):
    color: str


@dataclass
class BooleanDTO(BaseDTO):
    is_true: bool
