import random
import re

def clean_text(text: str) -> str:
    return re.sub(r"[^a-zA-Z ]", "", text).strip().lower()

def shuffle_word(word: str) -> str:
    letters = list(word)
    random.shuffle(letters)
    return "".join(letters)
