from dataclasses import dataclass

from src.pokemon.rarity import Rarity


@dataclass
class Card:
    name: str
    set_code: str
    card_set_number: int
    rarity: Rarity
