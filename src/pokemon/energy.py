from dataclasses import dataclass

from src.pokemon.card import Card


@dataclass
class Energy(Card):

    energy_type: str

    def __init__(
        self,
        name: str,
        set_code: str,
        card_set_number: int,
        rarity: str,
        energy_type: str,
    ) -> None:
        super().__init__(name, set_code, card_set_number, rarity)
        self.energy_type = energy_type
