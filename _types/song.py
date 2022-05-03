from typing import TypedDict

from utils import SeasonPeriod, SongTypes


class Song(TypedDict):
    id: int
    anime_id: int
    title: str
    artist: str
    album: str
    year: int
    season: SeasonPeriod
    duration: int
    preview_url: str
    open_spotify_url: str
    local_spotify_url: str
    song_type: SongTypes

