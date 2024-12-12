from dataclasses import dataclass


@dataclass
class Move:
    _name: str

    def __init__(self, name: str) -> None:
        self._name = name


# TODO: make cost object
@dataclass
class Attack(Move):
    _cost: str | None  # TODO: change to obj, some move don't have cost
    _effect: str | None
    _damage: int | None

    def __init__(
        self, name: str, cost: str | None, effect: str | None, damage: int | None
    ) -> None:
        super().__init__(name)
        self._cost = cost  # TODO: Should be Obj in the future
        self._effect = effect  # Not all moves have an effect
        self._damage = damage  # Not all moves do damage


class Ability(Move):
    def __init__(self, name: str, effect: str) -> None:
        super().__init__(name)
        self._effect: str = effect

    @property
    def effect(self) -> str:
        return self._effect
