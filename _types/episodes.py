from typing import Union, TypedDict, Dict


class Episodes(TypedDict):
    id: int
    anime_id: int
    number: int
    title: str
    video: str
    video_headers: Dict[str, str]
    locale: str
    quality: Union[int, None]
    format: str
    is_dub: bool
