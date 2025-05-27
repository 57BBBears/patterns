from typing import Literal

from implementation.translator import Translator
from implementation.transliterator import Transliterator


class TranslatorAdapter(Translator):
    """Allows to collaborate Translator and Transliterator."""

    def __init__(
        self,
        adaptee: Transliterator,
        native_lang: Literal["RU", "EN"],
        foreign_lang: Literal["RU", "EN"],
    ):
        self.adaptee = adaptee
        super().__init__(native_lang, foreign_lang)

    def translate(self, phrase: str) -> str:
        return self.adaptee.transliterate(phrase, self.foreign_lang)
