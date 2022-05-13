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

from typing import List, Union, Any, Optional, Dict
from dataclasses import dataclass


@dataclass(frozen=True)
class DataObj:
    """ This class converts the Dict output to an DataObj """

    # Return the current page of Objects, it can be changed by the `page` parameter in the request.
    current_page: int

    # Return the count of objects inside the current response.
    count: int

    # On List requests this will contain the objects given by the Api.
    documents: list

    # The last page that can be accessed.
    last_page: int

    def __repr__(self):
        """ This returns a stripped representation of the object """
        return f'<current_page={self.current_page} count={self.count} ' \
               f'last_page={self.last_page} documents={self.documents}>'


@dataclass(frozen=True)
class RateLimit:
    """
    This RateLimit objects contains the information of the ratelimit,
    later it can be useful to do something like a ratelimit-handler
    """

    # The Limit that was setted by the API owner
    limit: str

    # The remaining requests that can be made, will be reset every second
    remaining: str

    # How long until the reset of the remaining requests
    reset: str

    def __repr__(self):
        """ This returns a stripped representation of the object """
        return f'<limit={self.limit} remaining={self.remaining} reset={self.reset}>'


@dataclass(frozen=True)
class Context:
    """ This the "Data Holder", this class will be used to put the whole response to an object """

    # The ratelimit, can be used later for limiting stuff.
    ratelimit: RateLimit

    # The converted data that you get from the Api.
    data: Union[Any, List[Any]]

    # The status code from the response.
    status_code: int = 404

    # The message that is delivered with the response.
    message: str = 'Not found.'

    # The version that is used.
    version: str = '1'

    def __repr__(self):
        """ I know it's getting repetitive, but this returns a stripped representation of the object """
        return f'<status_code={self.status_code} message={self.message!r} data={self.data} version={self.version!r}>'


@dataclass(frozen=True)
class EpisodeObj:
    """ This class represents the Episode Object """

    # The episode id.
    id: int

    # The anime id that the episode belongs to.
    anime_id: int

    # The number of episodes.
    number: int

    # The title of the episode.
    title: str

    # The episodes original streaming url.
    video: str

    # The video's headers needed to navigate.
    video_headers: str

    # The episode's website related locale.
    locale: str

    # The quality of the episode.
    quality: Optional[int]

    # The format of the video.
    format: str

    # Is this episode dubbed?
    is_dub: bool

    def __repr__(self):
        return f'<id={self.id} anime_id={self.anime_id} number={self.number} locale={self.locale}>'


@dataclass(frozen=True)
class AnimeObj:
    """ This class represents the AnimeObj given by the Api """

    # The anime id
    id: int

    # The anime id on anilist.co
    anilist_id: int

    # The anime id on myanimelist.net
    mal_id: int

    # The anime id on themoviedb.org
    tmdb_id: int

    # The shows format destination
    format: int

    # The current status of the anime
    status: int

    # The titles organized by the locales
    titles: Dict[str, str]

    # The same as the titles but for descriptions
    descriptions: Dict[str, str]

    # The animes global start date
    start_date: Optional[str]

    # The known shows global end date
    end_date: Optional[str]

    # The weekly airing day
    weekly_airing_day: Optional[str]

    # The season that the shows has been released
    season_period: Optional[int]

    # The release year
    season_year: Optional[int]

    # The count for the episodes at the show
    episode_count: int

    # The average episode duration
    episode_duration: Optional[int]

    # The url to the Trailer
    # currently: YouTube and Dailymotion
    trailer_url: Optional[str]

    # The cover image url
    cover_image: str

    # Has the show a cover image?
    has_cover_image: bool

    # Cover color, represented as `HEX`
    cover_color: Optional[str]

    # The shows banner image
    banner_image: Optional[str]

    # The genres that the show is associated with
    genres: List[str]

    # A collection of all associated sagas to the show
    sagas: list

    # The show's precedent Animes id in story-line
    sequel: Optional[int]

    # The shows successive Animes id in story-lin
    prequel: Optional[int]

    # The score that the anime has, from 0 up to 100
    score: float

    # Is it NSFW?
    nsfw: bool

    # The shows recommended animes ids because similar. Ordered by descendent rating
    recommendations: Optional[List[int]]

    def __repr__(self) -> str:
        return f'<id={self.id} title={list(self.titles.values())[0]!r} ' \
               f'descriptions={[i for i in self.descriptions.keys()]} nsfw={self.nsfw}>'


@dataclass(frozen=True)
class SongObj:
    id: int
    anime_id: str
    title: str
    artist: str
    album: str
    year: int
    season: int
    duration: int
    preview_url: str
    open_spotify_link: str
    local_spotify_url: str
    type: int

    def __repr__(self) -> str:
        return f'<id={self.id} title={self.title!r} artist={self.artist!r}>'


@dataclass(frozen=True)
class UserSObj:
    id: int
    username: str
    role: int
    gender: int

    def __repr__(self) -> str:
        return f'<username={self.username} role={self.role} id={self.id} gender={self.gender}>'


@dataclass(frozen=True)
class UserBObj(UserSObj):
    email: str
    email_verified: bool
    avatar_tracker: str
    localization: str
    has_anilist: Optional[bool]
    has_mal: Optional[bool]

    def __repr__(self) -> str:
        return f'<id={self.id} username={self.username!r} email_verified={self.email_verified} role={self.role}>'


@dataclass(frozen=True)
class UserStoryObj:
    """ This class represents the UserStory's object """
    id: int
    user_id: int
    anime_id: str
    status: int
    current_episode: int
    current_episode_ticks: int

    def __repr__(self):
        return f'<id={self.id} user_id={self.user_id} status={self.status}>'
