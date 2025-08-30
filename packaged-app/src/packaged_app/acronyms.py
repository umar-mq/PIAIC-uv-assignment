from .utils import clean_text


def make_acronym(phrase: str) -> str:
    phrase = clean_text(phrase)
    words = phrase.split()
    if not words:
        return "N/A"
    return "".join(word[0].upper() for word in words)
