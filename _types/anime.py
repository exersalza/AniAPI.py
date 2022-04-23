#  MIT License
#
#  Copyright (c) 2022 by exersalza
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
from typing import TypedDict, Union, List, Any, Dict
from utils import AnimeFormat, AnimeStatus, AiringDays, SeasonPeriod


class Anime:
    id: int
    anilist_id: Union[int, None]
    mal_id: Union[int, None]
    tmdb_id: Union[int, None]
    format: AnimeFormat
    status: AnimeStatus
    titles: dict
    descriptions: dict
    start_date: Union[str, None]
    end_date: Union[str, None]
    weakly_airing_day: AiringDays
    season_period: SeasonPeriod
    season_year: Union[int, None]
    episodes_count: int
    episodes_duration: Union[int, None]
    trailer_url: Union[str, None]
    cover_image: str
    has_cover_image: bool
    cover_color: Union[str, None]
    banner_image: Union[str, None]
    genres: List[str]
    sagas: List[Dict[str, Any]]
    sequel: Union[int, None]
    prequel: Union[int, None]
    score: float
    nsfw: bool
    recommendations: List[int]
