"""This module defines the Stat class, which represents stats a pokemon can have.
"""

from enum import Enum, auto, unique


@unique
class Stat(Enum):
    """Enumeration, represent a stat a pokemon can have."""
    HP = auto()
    ATK = auto()
    DEF = auto()
    SPA = auto()
    SPD = auto()
    SPE = auto()

    def index(self) -> int:
        """
        Returns a stable 0-based index for this stat.
        """
        return STAT_TO_INDEX[self]

    def __str__(self) -> str:
        return f"{self.name} (stat) object"

MOVABLE_STATS = [
    Stat.ATK,
    Stat.DEF,
    Stat.SPA,
    Stat.SPD,
    Stat.SPE,
]

STATS = MOVABLE_STATS + [Stat.HP]

STAT_TO_INDEX = {t: i for i, t in enumerate(STATS)}


