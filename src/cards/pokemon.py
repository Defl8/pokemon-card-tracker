from src.cards.card import Card
from src.cards.move import Ability, Attack


class Pokemon(Card):
    def __init__(
        self,
        card_type: str,  # inherited
        name: str,  # inherited
        set: str,  # inherited
        rarity: str,
        pkmn_type: str,
        stage: str,
        hit_points: int,
        retreat_cost: str,  # TODO: make cost object
        weakness: str | None,  # TODO: make energy object,
        resistance: str | None,  # TODO: make energy object
        reg_mark: str,
        *moves: Attack | Ability,
    ) -> None:
        super().__init__(card_type, name, set, reg_mark, rarity)
        self.pkmn_type: str = pkmn_type
        self.stage: str = stage
        self.hit_points: int = hit_points
        self.moves: tuple[Attack | Ability, ...] = moves
        self.retreat_cost: str = retreat_cost
        self.weakness: str | None = weakness  # TODO: make energy object,
        self.resistance: str | None = resistance  # TODO: make energy object
