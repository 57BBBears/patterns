from implementation.image import Extent, Image


class ImageProxy(Image):
    """Image proxy with a default extent implementation."""

    def __init__(self, url: str, default_height: int = 100, default_width: int = 100):
        self._default_height = default_height
        self._default_width = default_width
        super().__init__(url)

    @property
    def extent(self) -> Extent:
        """Fake image extent without downloading the whole image."""
        return self._extent or self._get_extent()

    def _get_height(self) -> int:
        if not self._image:
            return self._default_height

        return super()._get_height()

    def _get_width(self) -> int:
        if not self._image:
            return self._default_width

        return super()._get_width()
