from interfaces.parcel import Parcel
from interfaces.post import Post


class StandardPost(Post):
    rate = 1

    def calculate_price(self, parcel: Parcel) -> int:
        return parcel.volume * self.rate
