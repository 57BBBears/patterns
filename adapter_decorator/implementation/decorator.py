from implementation.translator import Translator
from implementation.transliterator import Transliterator


def translate_adapter(adaptee: Transliterator):
    def decorator(cls):
        setattr(cls, "adaptee", adaptee)

        def translate(self, phrase: str) -> str:
            return self.adaptee.transliterate(phrase, self.foreign_lang)

        cls.translate = translate

        return cls

    return decorator


@translate_adapter(Transliterator())
class DecoratedTranslator(Translator):
    """Adds adaptor functionality to the Translator by implementing a decorator."""

    ...
