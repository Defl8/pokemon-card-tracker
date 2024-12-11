class Card:
    _type: str = ""
    _set: str = ""
    _allowed_card_types: tuple[str, ...] = ("pokemon", "trainer", "energy")
    _max_set_len: int = 3

    def __init__(self, card_type: str, name: str, set: str) -> None:
        self.type = card_type
        self.name: str = name
        self.set = set

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, card_type: str) -> None:
        if card_type.strip() not in Card._allowed_card_types:
            raise ValueError(f"Value {card_type} is not a valid card type.")
        self._type = card_type

    @property
    def set(self) -> str:
        return self._set

    @set.setter
    def set(self, set: str) -> None:
        if len(set) > Card._max_set_len:
            raise ValueError(f"Input set name {set} is too long.")
        self._set = set
