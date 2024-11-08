from dataclasses import dataclass

from src.pokemon.enums import Rarity, Type, string_to_enum_member
from src.db.sql import insert_into_table


@dataclass
class Card:
    """Store info about an indiviual card."""

    name: str
    set_code: str
    card_set_number: int
    type: Type
    rarity: Rarity
    amount: int

    def __init__(
        self,
        name: str,
        set_code: str,
        card_set_number: int,
        type: str,
        rarity: str,
        amount: int,
    ) -> None:
        self.name = name
        self.set_code = set_code
        self.card_set_number = card_set_number
        self.rarity = string_to_enum_member(rarity, Rarity)
        self.type = string_to_enum_member(type, Type)
        self.amount = amount

    def write_to_db(self, db_name: str):
        insert_statement: str = "insert into cards(name)"
