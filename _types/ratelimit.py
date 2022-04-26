from typing import TypedDict


class RateLimit(TypedDict):
    limit: str
    remaining: str
    reset: str
