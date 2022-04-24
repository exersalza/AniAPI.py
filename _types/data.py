from typing import Optional, List

from _types.anime import Anime


class Data:
    current_page: int
    count: int
    documents: List[Anime]
    last_page: Optional[int] = None
