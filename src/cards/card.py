from dataclasses import dataclass


@dataclass
class Card:
    name: str
    type: str
    set: str
    reg_mark: str
