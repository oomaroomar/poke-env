"""This module defines the Status class, which represents statuses a pokemon can be
afflicted with.
"""

from enum import Enum, auto, unique


@unique
class Status(Enum):
    """Enumeration, represent a status a pokemon can be afflicted with."""

    BRN = auto()
    FNT = auto()
    FRZ = auto()
    PAR = auto()
    PSN = auto()
    SLP = auto()
    TOX = auto()

    def index(self):
        return STATUS_TO_INDEX[self]

    def __str__(self) -> str:
        return f"{self.name} (status) object"

STATUS_STRINGS = [
    "brn",
    "frz",
    "psn",
    "tox",
    "par",
    "slp",
]

STATUSES = [Status[s.upper()] for s in STATUS_STRINGS]

STATUSES_W_FNT = STATUSES + [Status.FNT]

STATUS_TO_INDEX = {sts: i for i, sts in enumerate(STATUSES_W_FNT)}