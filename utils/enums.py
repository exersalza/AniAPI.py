#   MIT License
#  #
#   Copyright (c) 2022 by exersalza
#  #
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#  #
#   The above copyright notice and this permission notice shall be included in all
#   copies or substantial portions of the Software.
#  #
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#   SOFTWARE.

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


class UserStoryStatus(IntEnum):
    CURRENT = 0
    PLANNING = 1
    COMPLETED = 2
    DROPPED = 3
    PAUSED = 4
    REPEATING = 5
