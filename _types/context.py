from typing import TypedDict

from .data import Data
from .ratelimit import RateLimit


class Context(TypedDict):
    status_code: int
    message: str
    data: Data
    version: int
    ratelimit: RateLimit
