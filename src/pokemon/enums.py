from enum import Enum


class Rarity(Enum):
    NA = -1
    COMMON = 0
    UNCOMMON = 1
    RARE = 2
    REVERSE_HOLOFOIL = 3
    HOLOFOIL_RARE = 4
    DOUBLE_RARE = 5
    ULTRA_RARE = 6
    SECRET_RARE = 7


class Type(Enum):
    GRASS = 0
    RED = 1
    WATER = 2
    FIGHTING = 3
    LIGHTNING = 4
    PSYCHIC = 5
    DARK = 6
    DRAGON = 7


def parse_rarity(rarity_string: str) -> Rarity:
    """Takes input rarity string and converts to Rarity type from enum.

    Args:
    rarity_string(str): a string representing the rarity

    Returns:
    Rarity enum object. If input rarity is not valid then return NA member of Rarity.
    """
    cleaned_rarity_string: str = rarity_string.strip().replace(" ", "_").upper()
    rarity_names: list[str] = Rarity._member_names_
    if cleaned_rarity_string in rarity_names:
        return Rarity[cleaned_rarity_string]
    return Rarity.NA
