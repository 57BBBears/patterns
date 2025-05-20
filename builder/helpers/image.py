from typing import Protocol


class ImageProto(Protocol):
    """Protocol for getting image from string."""

    def get_image(self, query: str) -> str: ...


class ImageDownloader(ImageProto):
    def get_image(self, query: str) -> str:
        return f"https://api.test.com/image/{query}/"
