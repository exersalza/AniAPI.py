from .data import Data


class Context:
    status_code: int
    message: str
    data: Data
    version: int
