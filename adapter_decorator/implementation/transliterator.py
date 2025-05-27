from typing import Literal


class Transliterator:
    """Transliterates from Russian to English and vise versa.
    The class is incompatible with Translator class."""

    def __init__(self):
        self._en_ru_mapping = {
            # Vowels
            "a": "а",
            "e": "е",
            "i": "и",
            "o": "о",
            "u": "у",
            "y": "ы",
            "A": "А",
            "E": "Е",
            "I": "И",
            "O": "О",
            "U": "У",
            "Y": "Ы",
            # Consonants (direct mappings)
            "b": "б",
            "c": "к",
            "d": "д",
            "f": "ф",
            "g": "г",
            "h": "х",
            "j": "дж",
            "k": "к",
            "l": "л",
            "m": "м",
            "n": "н",
            "p": "п",
            "q": "к",
            "r": "р",
            "s": "с",
            "t": "т",
            "v": "в",
            "w": "в",
            "x": "кс",
            "z": "з",
            "B": "Б",
            "C": "К",
            "D": "Д",
            "F": "Ф",
            "G": "Г",
            "H": "Х",
            "J": "Дж",
            "K": "К",
            "L": "Л",
            "M": "М",
            "N": "Н",
            "P": "П",
            "Q": "К",
            "R": "Р",
            "S": "С",
            "T": "Т",
            "V": "В",
            "W": "В",
            "X": "Кс",
            "Z": "З",
            # Special combinations
            "ch": "ч",
            "sh": "ш",
            "zh": "ж",
            "th": "з",
            "ph": "ф",
            "Ch": "Ч",
            "Sh": "Ш",
            "Zh": "Ж",
            "Th": "З",
            "Ph": "Ф",
            "CH": "Ч",
            "SH": "Ш",
            "ZH": "Ж",
            "TH": "З",
            "PH": "Ф",
            # Soft sign for palatalization (optional)
            "'": "ь",
        }

        self._ru_en_mapping = {
            # Single letters
            "а": "a",
            "е": "e",
            "и": "i",
            "о": "o",
            "у": "u",
            "ы": "y",
            "А": "A",
            "Е": "E",
            "И": "I",
            "О": "O",
            "У": "U",
            "Ы": "Y",
            "б": "b",
            "в": "v",
            "г": "g",
            "д": "d",
            "ж": "zh",
            "з": "z",
            "й": "y",
            "к": "k",
            "л": "l",
            "м": "m",
            "н": "n",
            "п": "p",
            "р": "r",
            "с": "s",
            "т": "t",
            "ф": "f",
            "х": "h",
            "ц": "ts",
            "ч": "ch",
            "ш": "sh",
            "щ": "shch",
            "ъ": "",
            "ь": "'",
            "э": "e",
            "ю": "yu",
            "я": "ya",
            "Б": "B",
            "В": "V",
            "Г": "G",
            "Д": "D",
            "Ж": "Zh",
            "З": "Z",
            "Й": "Y",
            "К": "K",
            "Л": "L",
            "М": "M",
            "Н": "N",
            "П": "P",
            "Р": "R",
            "С": "S",
            "Т": "T",
            "Ф": "F",
            "Х": "H",
            "Ц": "Ts",
            "Ч": "Ch",
            "Ш": "Sh",
            "Щ": "Shch",
            "Ъ": "",
            "Ь": "'",
            "Э": "E",
            "Ю": "Yu",
            "Я": "Ya",
            # Special combinations (less common in reverse)
            "кс": "x",
            "дж": "j",
            "Кс": "X",
            "Дж": "J",
        }

    def transliterate(self, phrase: str, to_language: Literal["RU", "EN"]) -> str:
        match to_language:
            case "EN":
                result = "".join(
                    [self._ru_en_mapping.get(letter, " ") for letter in phrase]
                )
            case "RU":
                result = "".join(
                    [self._en_ru_mapping.get(letter, " ") for letter in phrase]
                )
            case _:
                raise ValueError

        return result
