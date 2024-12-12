class Card:
    def __init__(self, card_type: str, name: str, set: str, reg_mark: str) -> None:
        self._type: str = ""
        self.type: str = card_type
        self.name: str = name
        self.set: str = set
        self.reg_mark: str = reg_mark
