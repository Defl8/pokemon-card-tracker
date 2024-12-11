from src.cards.card import Card
from src.cards.move import Ability, Attack


class Pokemon(Card):
    def __init__(
        self,
        card_type: str,  # inherited
        name: str,  # inherited
        set: str,  # inherited
        pkmn_type: str,
        stage: str,
        hit_points: int,
        retreat_cost: str,  # TODO: make cost object
        weakness: str,  # TODO: make energy object
        *moves: Attack | Ability,
    ) -> None:
        super().__init__(card_type, name, set)
        self.pkmn_type: str = pkmn_type
        self.stage: str = stage
        self.hit_points: int = hit_points
        self.moves: tuple[Attack | Ability, ...] = moves
