from typing import Literal


class Translator:
    """Base class for a translation."""

    def __init__(
        self, native_lang: Literal["RU", "EN"], foreign_lang: Literal["RU", "EN"]
    ):
        self.native_lang: Literal["RU", "EN"] = native_lang
        self.foreign_lang: Literal["RU", "EN"] = foreign_lang

    def translate(self, phrase: str) -> str: ...
