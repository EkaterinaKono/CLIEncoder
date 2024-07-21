import string
from abc import ABC, abstractmethod


def letter_range(ch1: str, ch2: str) -> str:
    return ''.join([chr(i) for i in range(ord(ch1), ord(ch2) + 1)])


ENG_LETTERS_UPPER = string.ascii_uppercase
ENG_LETTERS_LOWER = string.ascii_lowercase
RUS_LETTERS_UPPER = letter_range("А", "Я")
RUS_LETTERS_LOWER = letter_range("а", "я")
ALL_LETTERS = [ENG_LETTERS_UPPER, ENG_LETTERS_LOWER, RUS_LETTERS_UPPER, RUS_LETTERS_LOWER]


def get_index(ch: str) -> int:
    for letters in ALL_LETTERS:
        index = letters.find(ch)
        if index != -1:
            return index
    return -1


def shift(ch: str, shift_amount: int) -> str:
    for letters in ALL_LETTERS:
        index = letters.find(ch)
        if index != -1:
            new_index = (index + shift_amount) % len(letters)
            new_ch = letters[new_index]
            return new_ch
    return ch


class BaseEncoder(ABC):
    _key = None

    def __init__(self, key):
        self.key = key

    @property
    def key(self):
        return self._key

    @key.setter
    @abstractmethod
    def key(self, new_key):
        self._key = new_key

    @abstractmethod
    def encode(self, text: str):
        pass

    @abstractmethod
    def decode(self, text: str):
        pass
