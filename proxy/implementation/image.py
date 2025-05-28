from dataclasses import dataclass
from urllib.parse import ParseResult, parse_qs, urlparse

type Kb = int


@dataclass
class Extent:
    height: int
    width: int
    size: Kb


class Image:
    def __init__(self, url: str):
        self.url: ParseResult = urlparse(url)
        self._image: bytes | None = None
        self._extent: Extent | None = None

    @property
    def extent(self) -> Extent | None:
        if not self._extent:
            self.download()

        return self._extent

    @property
    def image(self) -> bytes | None:
        if not self._image:
            self.download()

        return self._image

    def download(self):
        """Get the image."""
        if image_name := parse_qs(self.url.query).get("image"):
            self._image = image_name[0].encode("utf-8")
            self._extent = self._get_extent()
        else:
            raise ValueError("Image is not found.")

    def _get_extent(self) -> Extent:
        return Extent(
            height=self._get_height(), width=self._get_width(), size=self._get_size()
        )

    def _get_height(self) -> int:
        return len(self.image) if self.image else 0

    def _get_width(self) -> int:
        return len(self.image) if self.image else 0

    def _get_size(self) -> Kb:
        return self._get_height() * self._get_width()
