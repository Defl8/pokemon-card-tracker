class Card:
    def __init__(self, name: str, type: str) -> None:
        self.name: str = name
        self._type: str = type

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, card_type: str) -> None:
        allowed_types: tuple[str, ...] = ("pokemon", "trainer", "energy")
        if card_type.strip() not in allowed_types:
            raise ValueError(f"Value {card_type} is not a valid card type.")
        self._type = card_type
