class Card:
    def __init__(self, card_type: str, name: str) -> None:
        self._card_type: str = card_type
        self.name: str = name

    @property
    def type(self) -> str:
        return self._card_type

    @type.setter
    def type(self, card_type: str) -> None:
        allowed_card_types: tuple[str, ...] = ("pokemon", "trainer", "energy")
        if card_type.strip() not in allowed_card_types:
            raise ValueError(f"Value {card_type} is not a valid card type.")
        self._card_type = card_type
