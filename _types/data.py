from typing import Optional, List, TypedDict

from _types.anime import Anime


class Data(TypedDict):
    current_page: int
    count: int
    documents: List[Anime]
    last_page: Optional[int]
