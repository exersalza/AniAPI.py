from typing import TypedDict

from .ratelimit import RateLimit
from .data import Data


class Context(TypedDict):
    status_code: int
    message: str
    data: Data
    version: int
    ratelimit: RateLimit
