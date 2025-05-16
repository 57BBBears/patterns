from abc import ABC, abstractmethod

from .parcel import Parcel


class Post(ABC):
    @abstractmethod
    def calculate_price(self, parcel: Parcel) -> int: ...
