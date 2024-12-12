from src.cards.card import Card


class Energy(Card):
    def __init__(
        self,
        card_type: str,
        name: str,
        set: str,
        reg_mark: str,
        rarity: str,
        eng_type: str,
        is_promo: bool,
        is_acespec: bool = False,
    ) -> None:
        super().__init__(
            card_type, name, set, reg_mark, rarity, is_promo, legality=None
        )
        self.eng_type: str = eng_type
        self.is_acespec: bool = is_acespec
