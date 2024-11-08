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


def string_to_enum_member(
    rarity_string: str, enumeration: Rarity | Type
) -> Rarity | Type:
    """Takes input rarity string and converts to Rarity type from enum.

    Args:
    rarity_string(str): a string representing the rarity

    Returns:
    Rarity enum object. If input rarity is not valid then return NA member of Rarity.
    """
    cleaned_string: str = rarity_string.strip().replace(" ", "_").upper()
    enum_member_names: list[str] = enumeration._member_names_
    if cleaned_string in enum_member_names:
        return enumeration[cleaned_string]
    else:
        raise NotImplementedError
