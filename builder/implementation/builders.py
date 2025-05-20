from urllib.parse import ParseResult, urlparse

from helpers.image import ImageProto
from interfaces.builder import DocumentBuilder


class HTMLBuilder(DocumentBuilder):
    """Builds html version of a document."""

    def __init__(self):
        self.template = ""

    def build_header(self, title: str = ""):
        self.template += f"""
            <html>
                <head>
                  <title>HTML version{" of " + title if title else ""}</title>
                </head>
                <body>
        """

    def build_title(self, title: str):
        self.template += f"<h1>{title}</h1>\n"

    def build_content(self, content: str):
        self.template += f"<p>{content}</p>\n"

    def build_footer(self, copyright: str = ""):
        self.template += f"""
                    <footer>{"© " + copyright if copyright else ""}</footer>
                </body>
            </html>
        """

    def reset(self):
        self.template = ""

    def get_result(self) -> str:
        return self.template


class ImageBuilder(DocumentBuilder):
    """Builds image representation of a document."""

    def __init__(self, image_api: ImageProto):
        self.image_api = image_api
        self.image = ""

    def build_title(self, title: str):
        self.image = self.image_api.get_image(title)

    def get_result(self) -> ParseResult:
        return urlparse(self.image)
