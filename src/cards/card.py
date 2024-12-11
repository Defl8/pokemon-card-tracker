class Card:
    def __init__(self, card_type: str, name: str, set: str) -> None:
        self._type: str = ""
        self.name: str = name
        self._set: str = set

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, card_type: str) -> None:
        allowed_card_types: tuple[str, ...] = ("pokemon", "trainer", "energy")
        if card_type.strip() not in allowed_card_types:
            raise ValueError(f"Value {card_type} is not a valid card type.")
        self._type = card_type
