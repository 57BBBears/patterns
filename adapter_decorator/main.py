from implementation.adapter import TranslatorAdapter
from implementation.decorator import DecoratedTranslator
from implementation.transliterator import Transliterator


def adapter():
    transliterator = Transliterator()
    en_ru_adapter = TranslatorAdapter(transliterator, "EN", "RU")
    ru_en_adapter = TranslatorAdapter(transliterator, "RU", "EN")

    print("Adapter")
    print("EN -> RU", en_ru_adapter.translate("Hello"))
    print("RU -> EN", ru_en_adapter.translate("Привет"))


def decorator():
    en_ru_adapter = DecoratedTranslator("EN", "RU")
    ru_en_adapter = DecoratedTranslator("RU", "EN")

    print("Decorator")
    print("EN -> RU", en_ru_adapter.translate("Hello"))
    print("RU -> EN", ru_en_adapter.translate("Привет"))


if __name__ == "__main__":
    adapter()

    decorator()
