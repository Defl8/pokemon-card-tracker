class InvalidCardType(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidCardRarity(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
