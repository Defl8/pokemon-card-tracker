from dataclasses import dataclass

from src.pokemon.rarity import Rarity


@dataclass
class Card:
    name: str
    set_code: str
    card_set_number: int
    rarity: Rarity

    def __init__(self, name: str, set_code: str, card_set_number: int, rarity: str) -> None:
        self.name = name
        self.set_code = set_code
        self.card_set_number = card_set_number
        self.rarity =
