from dataclasses import dataclass


@dataclass
class Move:
    _name: str

    def __init__(self, name: str) -> None:
        self._name = name


# TODO: make cost object
@dataclass
class Attack(Move):
    def __init__(
        self,
        name: str,
        cost: str,
    ) -> None:
        super().__init__(name)
