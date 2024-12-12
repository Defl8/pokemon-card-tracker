from dataclasses import dataclass

from src.cards.legality import Legality


@dataclass
class Card:
    name: str
    type: str
    set: str
    reg_mark: str
    rarity: str
    is_promo: bool
    legality: Legality | None
