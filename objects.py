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


class DataObj:
    """ This class converts the Dict output to an DataObj """

    def __init__(self, **kwa):
        self.__current_page = kwa.get('current_page')
        self.__count = kwa.get('count')
        self.__documents = kwa.get('documents')
        self.__last_page = kwa.get('last_page')

    @property
    def current_page(self) -> int:
        """ Return the current page of Objects, it can be changed by the `page` parameter in the request """
        return self.__current_page

    @property
    def count(self) -> int:
        """ Return the count of objects inside the current response. """
        return self.__count

    @property
    def documents(self) -> list:
        """ On List requests this will contain the objects given by the Api. """
        return self.__documents

    @property
    def last_page(self) -> int:
        """ The last page that can be accessed """
        return self.__last_page

    def __repr__(self):
        """ This returns a stripped representation of the object """
        return f'<current_page={self.current_page} count={self.count} ' \
               f'last_page={self.last_page} documents={self.documents}>'


class RateLimit:
    def __init__(self, limit: str, remaining: str, reset: str):
        """
        This RateLimit objects contains the information of the ratelimit,
        later it can be useful to do something like a ratelimit-handler
        """

        self.__limit = limit
        self.__remaining = remaining
        self.__reset = reset

    @property
    def limit(self) -> str:
        """ The Limit that was setted by the API owner """
        return self.__limit

    @property
    def remaining(self) -> str:
        """ The remaining requests that can be made, will be reset every second """
        return self.__remaining

    @property
    def reset(self) -> str:
        """ How long until the reset of the remaining requests """
        return self.__reset

    def __repr__(self):
        """ This returns a stripped representation of the object """
        return f'<limit={self.__limit} remaining={self.__remaining} reset={self.__reset}>'


class Context:
    def __init__(self, **kwa):  # Create a Non-changeable object
        """
        This is the Basic Context Object for the response
        """

        self.__status_code = kwa.get('status_code', 404)
        self.__message = kwa.get('message', 'Not Found')
        self.__data = kwa.get('data', {})
        self.__version = kwa.get('version', '1')
        self.__ratelimit = kwa.get('ratelimit')

    @property
    def status_code(self) -> int:
        """ The status code of the response, useful for error handling """
        return self.__status_code

    @property
    def message(self) -> str:
        """ The message that is given by the api, often times it will contain useful information """
        return f'{self.__message!r}'

    @property
    def data(self) -> Union[Any, List[Any]]:
        """ The data that is given by the api, it can be a list of objects or a single object """
        return self.__data

    @property
    def version(self) -> str:
        """ The current version of the api """
        return self.__version

    @property
    def ratelimit(self) -> RateLimit:
        """ The ratelimit for the next responses """
        return self.__ratelimit

    def __repr__(self):
        """ I know it's getting repetitive, but this returns a stripped representation of the object """
        return f'<status_code={self.status_code} message={self.message!r} data={self.data} version={self.version!r}>'


class EpisodeObj:
    def __init__(self, **kwa):
        """ This class represents the Episode Object """
        self.__id = kwa.get('id')
        self.__anime_id = kwa.get('anime_id')
        self.__number = kwa.get('number')
        self.__title = kwa.get('title')
        self.__video = kwa.get('video')
        self.__video_headers = kwa.get('video_headers')
        self.__locale = kwa.get('locale')
        self.__quality = kwa.get('quality')
        self.__format = kwa.get('format')
        self.__is_dub = kwa.get('is_dub')

    @property
    def id(self) -> int:
        """ The id of the episode """
        return self.__id

    @property
    def anime_id(self) -> int:
        """ The id of the anime that the episode belongs to """
        return self.__anime_id

    @property
    def number(self) -> int:
        """ The number of the episode """
        return self.__number

    @property
    def title(self) -> str:
        """ The title of the episode """
        return self.__title

    @property
    def video(self) -> str:
        """ The video url of the episode """
        return self.__video

    @property
    def video_headers(self) -> str:
        """ The video headers of the episode """
        return self.__video_headers

    @property
    def locale(self) -> str:
        """ The locale of the episode """
        return self.__locale

    @property
    def quality(self) -> str:
        """ The quality of the episode """
        return self.__quality

    @property
    def format(self) -> str:
        """ The format of the episode """
        return self.__format

    @property
    def is_dub(self) -> bool:
        """ Whether the episode is a dub or not """
        return self.__is_dub

    def __repr__(self):
        return f'<id={self.__id} anime_id={self.__anime_id} number={self.__number} locale={self.__locale}>'


class AnimeObj:
    def __init__(self, **kwa):
        """ This class represents the Anime Object """
        self.__id = kwa.get('id')
        self.__anilist_id = kwa.get('anilist_id')
        self.__mal_id = kwa.get('mal_id')
        self.__tmdb_id = kwa.get('tmdb_id')
        self.__format = kwa.get('format')
        self.__status = kwa.get('status')
        self.__titles = kwa.get('titles')
        self.__descriptions = kwa.get('descriptions')
        self.__start_date = kwa.get('start_date')
        self.__end_date = kwa.get('end_date')
        self.__weakly_airing_day = kwa.get('weakly_airing_day')
        self.__season_period = kwa.get('season_period')
        self.__season_year = kwa.get('season_year')
        self.__episodes_count = kwa.get('episodes_count')
        self.__episodes_duration = kwa.get('episodes_duration')
        self.__trailer_url = kwa.get('trailer_url')
        self.__cover_image = kwa.get('cover_image')
        self.__has_cover_image = kwa.get('has_cover_image')
        self.__cover_color = kwa.get('cover_color')
        self.__banner_image = kwa.get('banner_image')
        self.__genres = kwa.get('genres')
        self.__sagas = kwa.get('sagas')
        self.__sequel = kwa.get('sequel')
        self.__prequel = kwa.get('prequel')
        self.__score = kwa.get('score')
        self.__nsfw = kwa.get('nsfw')
        self.__recommendations = kwa.get('recommendations')

    @property
    def id(self) -> int:
        """ The id of the anime """
        return self.__id

    @property
    def anilist_id(self) -> int:
        """ The id of the anime on Anilist """
        return self.__anilist_id

    @property
    def mal_id(self) -> int:
        """ The id of the anime on MyAnimeList """
        return self.__mal_id

    @property
    def tmdb_id(self) -> int:
        """ The id of the anime on TheMovieDatabase """
        return self.__tmdb_id

    @property
    def format(self) -> str:
        """ The format of the anime, reference can be found at utils.enums.AnimeFormat """
        return self.__format

    @property
    def status(self) -> str:
        """ The status of the anime, status reference can be inside the utils.enums.AnimeStatus enum """
        return self.__status

    @property
    def titles(self) -> dict:
        """ The titles of the anime, often times you will find the `rj` inside it """
        return self.__titles

    @property
    def descriptions(self) -> Dict[str, str]:
        """ The description of the anime """
        return self.__descriptions

    @property
    def start_date(self) -> str:
        """ The start date of the anime """
        return self.__start_date

    @property
    def end_date(self) -> str:
        """ The end date of the anime """
        return self.__end_date

    @property
    def weakly_airing_day(self) -> str:
        """ The weakly airing day of the anime """
        return self.__weakly_airing_day

    @property
    def season_period(self) -> str:
        """ The season period of the anime """
        return self.__season_period

    @property
    def season_year(self) -> str:
        """ The season year of the anime """
        return self.__season_year

    @property
    def episodes_count(self) -> int:
        """ The episodes count of the anime """
        return self.__episodes_count

    @property
    def episodes_duration(self) -> int:
        """ The episodes duration of the anime """
        return self.__episodes_duration

    @property
    def trailer_url(self) -> str:
        """ The trailer url of the anime """
        return self.__trailer_url

    @property
    def cover_image(self) -> str:
        """ The cover image of the anime """
        return self.__cover_image

    @property
    def has_cover_image(self) -> bool:
        """ Whether the anime has a cover image or not """
        return self.__has_cover_image

    @property
    def cover_color(self) -> str:
        """ The cover color of the anime """
        return self.__cover_color

    @property
    def banner_image(self) -> str:
        """ The banner image of the anime """
        return self.__banner_image

    @property
    def genres(self) -> list:
        """ The genres of the anime """
        return self.__genres

    @property
    def sagas(self) -> list:
        """ The sagas of the anime """
        return self.__sagas

    @property
    def sequel(self) -> int:
        """ The sequel of the anime """
        return self.__sequel

    @property
    def prequel(self) -> int:
        """ The prequel of the anime """
        return self.__prequel

    @property
    def score(self) -> float:
        """ The score of the anime """
        return self.__score

    @property
    def nsfw(self) -> bool:
        """ Whether the anime is nsfw or not """
        return self.__nsfw

    @property
    def recommendations(self) -> list:
        """ A list of recommendations of the anime """
        return self.__recommendations

    def __repr__(self) -> str:
        return f'<id={self.id} title={list(self.titles.values())[0]!r} ' \
               f'descriptions={[i for i in self.descriptions.keys()]} nsfw={self.nsfw}>'


class SongObj:
    def __init__(self, **kwa):
        """  The song object """
        self.__id = kwa.get('id')
        self.__anime_id = kwa.get('anime_id')
        self.__title = kwa.get('title')
        self.__artist = kwa.get('artist')
        self.__album = kwa.get('album')
        self.__year = kwa.get('year')
        self.__season = kwa.get('season')
        self.__duration = kwa.get('duration')
        self.__preview_url = kwa.get('preview_url')
        self.__open_spotify_url = kwa.get('open_spotify_url')
        self.__local_spotify_url = kwa.get('local_spotify_url')
        self.__type = kwa.get('type')

    @property
    def id(self) -> int:
        """ The id of the song """
        return self.__id

    @property
    def anime_id(self) -> int:
        """ The anime id that is related to the song """
        return self.__anime_id

    @property
    def title(self) -> str:
        """ The title of the song """
        return self.__title

    @property
    def artist(self) -> str:
        """ The artist of the song """
        return self.__artist

    @property
    def album(self) -> str:
        """ The album of the song """
        return self.__album

    @property
    def year(self) -> int:
        """ In which year the song got released """
        return self.__year

    @property
    def season(self) -> str:
        """ The season the song got released in """
        return self.__season

    @property
    def duration(self) -> int:
        """ The duration of the song in milliseconds. """
        return self.__duration

    @property
    def preview_url(self) -> str:
        """ The preview url of the song """
        return self.__preview_url

    @property
    def open_spotify_url(self) -> str:
        """ The open spotify url of the song """
        return self.__open_spotify_url

    @property
    def local_spotify_url(self) -> str:
        """ The local spotify url of the song """
        return self.__local_spotify_url

    @property
    def type(self) -> str:
        """ The type of the song """
        return self.__type

    def __repr__(self) -> str:
        return f'<id={self.id} title={self.title!r} artist={self.artist!r}>'


class UserSObj:
    def __init__(self, **kwa):
        self.__username = kwa.get('username')
        self.__role = kwa.get('role')
        self.__gender = kwa.get('gender')
        self.__id = kwa.get('id')

    @property
    def username(self) -> str:
        """ The username of the user """
        return self.__username

    @property
    def role(self) -> int:
        """ The role of the user, usually its 0 but for mods or admins its 1 and 2"""
        return self.__role

    @property
    def gender(self) -> int:
        """ The gender, 0: Not given, 1: Male, 2: Female """
        return self.__gender

    @property
    def id(self) -> int:
        """ The unique identifier of the user on AniApi.com """
        return self.__id

    def __repr__(self) -> str:
        return f'<username={self.username} role={self.role} id={self.id} gender={self.gender}>'


class UserBObj(UserSObj):
    def __init__(self, **kwa):
        """ The basic User object representation """
        super().__init__(**kwa)

        self.__email = kwa.get('email')
        self.__email_verified = kwa.get('email_verified')
        self.__avatar_tracker = kwa.get('avatar_tracker')
        self.__localization = kwa.get('localization')
        self.__has_anilist = kwa.get('has_anilist')
        self.__has_mal = kwa.get('has_mal')

    @property
    def email(self) -> str:
        """ |CONFIDENTIAL| The email of the user """
        return self.__email

    @property
    def email_verified(self) -> bool:
        """ |CONFIDENTIAL| Whether the email is verified or not """
        return self.__email_verified

    @property
    def avatar_tracker(self) -> Optional[str]:
        """ This will be only used inside the auth me requests """
        return self.__avatar_tracker

    @property
    def localization(self) -> str:
        """ |CONFIDENTIAL| The localization of the user """
        return self.__localization

    @property
    def has_anilist(self) -> Optional[bool]:
        """ Whether the user has anilist or not """
        return self.__has_anilist

    @property
    def has_mal(self) -> Optional[bool]:
        """ Whether the user has MyAnimeList or not """
        return self.__has_mal

    def __repr__(self) -> str:
        return f'<id={self.id} username={self.username!r} email_verified={self.email_verified}>'


class UserStoryObj:
    """ This class represents the UserStory's object """
    def __init__(self, **kwa):
        self.__id = kwa.get('id')
        self.__user_id = kwa.get('user_id')
        self.__anime_id = kwa.get('anime_id')
        self.__status = kwa.get('status')
        self.__current_episodes = kwa.get('current_episodes')
        self.__current_episode_ticks = kwa.get('current_episode_ticks')

    @property
    def _id(self) -> int:
        """ The id of the UserStory """
        return self.__id

    @property
    def user_id(self) -> int:
        """ The user that belongs the UserStory to """
        return self.__user_id

    @property
    def anime_id(self) -> str:
        """ The anime_id from the story """
        return self.__anime_id

    @property
    def status(self) -> int:
        """ The watching status """
        return self.__status

    @property
    def current_episode(self) -> int:
        """ Current episode watching progress """
        return self.__current_episodes

    @property
    def current_episode_ticks(self) -> int:
        """ The UserStory's `current_episode` watching time in milliseconds """
        return self.__current_episode_ticks

    def __repr__(self):
        return f'<id={self._id} user_id={self.user_id} status={self.status}>'
