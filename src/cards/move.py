from dataclasses import dataclass


@dataclass
class Move:
    _name: str

    def __init__(self, name: str) -> None:
        self._name = name


# TODO: make cost object
@dataclass
class Attack(Move):
    _cost: str  # TODO: change to obj
    _effect: str | None
    _damage: int | None

    def __init__(
        self, name: str, cost: str, effect: str | None, damage: int | None
    ) -> None:
        super().__init__(name)
        self._cost = cost  # TODO: Should be Obj in the future
        self._effect = effect  # Not all moves have an effect
        self._damage = damage  # Not all moves do damage
