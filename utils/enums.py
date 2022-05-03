from enum import IntEnum


class AnimeFormat(IntEnum):
    TV = 0
    TV_SHORT = 1
    MOVIE = 2
    SPECIAL = 3
    OVA = 4
    ONA = 5
    MUSIC = 6


class AnimeStatus(IntEnum):
    FINISHED = 0
    RELEASING = 1
    NOT_YET_RELEASED = 2
    CANCELLED = 3


class SeasonPeriod(IntEnum):
    WINTER = 0
    SPRING = 1
    SUMMER = 2
    FALL = 3
    UNKNOWN = 4


class AiringDays(IntEnum):
    Sunday = 0
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6


class SongTypes(IntEnum):
    OPENING = 0
    ENDING = 1
    NONE = 2
