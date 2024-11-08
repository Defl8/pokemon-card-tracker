from dataclasses import dataclass

from src.pokemon.enums import Rarity, Type, string_to_enum_member


@dataclass
class Card:
    """Store info about an indiviual card."""

    name: str
    set_code: str
    card_set_number: int
    type: Type
    rarity: Rarity

    def __init__(
        self, name: str, set_code: str, card_set_number: int, type: str, rarity: str
    ) -> None:
        self.name = name
        self.set_code = set_code
        self.card_set_number = card_set_number
        self.rarity = string_to_enum_member(rarity, Rarity)
        self.type = string_to_enum_member(type, Type)
