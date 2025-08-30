from wordfreq import zipf_frequency
from itertools import permutations
from .utils import clean_text


def is_valid_word(word: str) -> bool:
    return zipf_frequency(word, "en") > 0


def make_anagrams(word: str, limit: int = 5) -> list[str]:
    word = clean_text(word).replace(" ", "")
    if not word:
        return ["No valid letters to shuffle."]

    perms = set("".join(p) for p in permutations(word))

    valid = [p for p in perms if is_valid_word(p) and p.lower() != word.lower()]

    if not valid:
        return ["No valid anagrams found."]

    return valid[:limit]
