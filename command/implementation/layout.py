from enum import StrEnum


class Shape(StrEnum):
    CIRCLE = "()"
    SQUARE = "[]"
    TRIANGLE = "/\\"
    STAR = "*"


class Layout:
    """Receiver of commands."""

    def __init__(self, text: str = "", shape: Shape | None = None):
        self.current_text = text
        self.current_element = shape

    def draw(self):
        print(self.current_element if self.current_element else "...")

    def text(self):
        print(self.current_text)
