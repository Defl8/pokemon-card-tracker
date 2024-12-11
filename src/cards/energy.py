from src.cards.card import Card


class Energy(Card):
    _energy_types: tuple[str, ...] = (
        "Fire",
        "Water",
        "Grass",
        "Electric",
        "Fighting",
        "Darkness",
        "Psychic",
        "Metal",
        "Fairy",
        "Special",
    )

    def __init__(
        self,
        card_type: str,
        name: str,
        set: str,
        eng_type: str,
        is_acespec: bool = False,
    ) -> None:
        super().__init__(card_type, name, set)
        self._eng_type: str = ""
        self.is_acespec: bool = is_acespec

    @property
    def eng_type(self) -> str:
        return self._eng_type

    @eng_type.setter
    def eng_type(self, eng_type: str) -> None:
        if eng_type not in Energy._energy_types:
            raise ValueError(f"Energy type {eng_type} is not valid.")
        self._eng_type = "Special" if self.is_acespec else eng_type
