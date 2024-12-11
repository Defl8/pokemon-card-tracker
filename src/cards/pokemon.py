from src.cards.card import Card


class Pokemon(Card):
    def __init__(
        self,
        card_type: str,
        name: str,
        pkmn_type: str,
        stage: str,
        hit_points: int,
    ) -> None:
        super().__init__(card_type, name)
        self._card_type: str = card_type
        self.name: str = name
        self.pkmn_type: str = pkmn_type
        self.stage: str = stage
        self.hit_points: int = hit_points
