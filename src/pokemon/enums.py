from enum import Enum
from typing import TypeVar

from src.error.exceptions import InvalidCardType, InvalidCardRarity


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


Variant = TypeVar("Variant", Rarity, Type)


def string_to_enum_member(string_member: str, enumeration: type[Variant]) -> Variant:
    """Takes input string and checks if it is an acceptable enum member.

    Args:
    string_member(str): a string representing the member of an enum.

    Returns:
    Enum member is if string is valid. Throws InvalidCardRarity or InvalidCardType if invalid.
    """
    try:
        enum_member: Variant = getattr(enumeration, string_member)
    except AttributeError as err:
        if isinstance(enumeration, Rarity):
            raise InvalidCardRarity(
                f"{string_member} is not apart of acceptable rarities."
            )
        else:
            raise InvalidCardType(f"{string_member} is not apart of acceptable types.")
    return enum_member


def variant_to_int(var: Rarity | Type) -> int:
    """Function to get the value of the enum of type Variant.

    Args:
    var(Variant): Object with enum value.

    Returns:
    int represented by the enum member.
    """
    return var.value
