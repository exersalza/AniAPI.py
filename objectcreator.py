from typing import List, Union, Any


class DataObj:
    """ This class converts the Dict output to an DataObj """

    def __init__(self, **kwargs):
        self.__current_page = kwargs.get('current_page')
        self.__count = kwargs.get('count')
        self.__documents = kwargs.get('documents')
        self.__last_page = kwargs.get('last_page')

    @property
    def current_page(self) -> int:
        """
        Return the current page of Objects, it can be changed by the `page` parameter in the request
        """
        return self.__current_page

    @property
    def count(self) -> int:
        """
        Return the count of objects inside the current response.
        """
        return self.__count

    @property
    def documents(self) -> List[object]:
        """
        On List requests this will contain the objects given by the Api.
        """
        return self.__documents

    @property
    def last_page(self) -> int:
        """
        The last page that can be accessed
        """
        return self.__last_page

    def __repr__(self):
        """ This returns a stripped representation of the object """
        return f'<current_page={self.current_page} count={self.count} last_page={self.last_page} documents={self.documents}>'


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
        """
        The Limit that was setted by the API owner
        """
        return self.__limit

    @property
    def remaining(self) -> str:
        """
        The remaining requests that can be made, will be reset every second
        """
        return self.__remaining

    @property
    def reset(self) -> str:
        """
        How long until the reset of the remaining requests
        """
        return self.__reset

    def __repr__(self):
        """
        This returns a stripped representation of the object
        """
        return f'<limit={self.__limit} remaining={self.__remaining} reset={self.__reset}>'


class Context:
    def __init__(self, **kwargs):  # Create a Non-changeable object
        """
        This is the Basic Context Object for the response
        """

        self.__status_code = kwargs.get('status_code', 404)
        self.__message = kwargs.get('message', 'Not Found')
        self.__data = kwargs.get('data', {})
        self.__version = kwargs.get('version', '1')
        self.__ratelimit = kwargs.get('ratelimit', None)

    @property
    def status_code(self) -> int:
        """
        The status code of the response, useful for error handling
        """
        return self.__status_code

    @property
    def message(self) -> str:
        """
        The message that is given by the api, often times it will contain useful information
        """
        return f'{self.__message!r}'

    @property
    def data(self) -> Union[object, DataObj]:
        """
        The data that is given by the api, it can be a list of objects or a single object
        """
        return self.__data

    @property
    def version(self) -> str:
        """
        The current version of the api
        """
        return self.__version

    @property
    def ratelimit(self) -> RateLimit:
        """
        The ratelimit for the next responses
        """
        return self.__ratelimit

    def __repr__(self):
        """
        I know it's getting repetitive, but this returns a stripped representation of the object
        """

        return f'<status_code={self.__status_code} message={self.__message!r} data={self.__data} version={self.__version!r}>'


class EpisodeObj:
    def __init__(self, **kwargs):
        self.__id = kwargs.get('id')
        self.__anime_id = kwargs.get('anime_id')
        self.__number = kwargs.get('number')
        self.__title = kwargs.get('title')
        self.__video = kwargs.get('video')
        self.__video_headers = kwargs.get('video_headers')
        self.__locale = kwargs.get('locale')
        self.__quality = kwargs.get('quality')
        self.__format = kwargs.get('format')
        self.__is_dub = kwargs.get('is_dub')

    @property
    def id(self) -> int:
        return self.__id

    @property
    def anime_id(self) -> int:
        return self.__anime_id

    @property
    def number(self) -> int:
        return self.__number

    @property
    def title(self) -> str:
        return self.__title

    @property
    def video(self) -> str:
        return self.__video

    @property
    def video_headers(self) -> str:
        return self.__video_headers

    @property
    def locale(self) -> str:
        return self.__locale

    @property
    def quality(self) -> str:
        return self.__quality

    @property
    def format(self) -> str:
        return self.__format

    @property
    def is_dub(self) -> bool:
        return self.__is_dub

    def __repr__(self):
        return f'<id={self.__id} anime_id={self.__anime_id} number={self.__number} locale={self.__locale}>'


class AnimeObj:
    def __init__(self, **kwargs):
        self.__id = kwargs.get('id')
        self.__anilist_id = kwargs.get('anilist_id')
        self.__mal_id = kwargs.get('mal_id')
        self.__tmdb_id = kwargs.get('tmdb_id')
        self.__format = kwargs.get('format')
        self.__status = kwargs.get('status')
        self.__titles = kwargs.get('titles')
        self.__description = kwargs.get('description')
        self.__start_date = kwargs.get('start_date')
        self.__end_date = kwargs.get('end_date')
        self.__weakly_airing_day = kwargs.get('weakly_airing_day')
        self.__season_period = kwargs.get('season_period')
        self.__season_year = kwargs.get('season_year')
        self.__episodes_count = kwargs.get('episodes_count')
        self.__episodes_duration = kwargs.get('episodes_duration')
        self.__trailer_url = kwargs.get('trailer_url')
        self.__cover_image = kwargs.get('cover_image')
        self.__has_cover_image = kwargs.get('has_cover_image')
        self.__cover_color = kwargs.get('cover_color')
        self.__banner_image = kwargs.get('banner_image')
        self.__genres = kwargs.get('genres')
        self.__sagas = kwargs.get('sagas')
        self.__sequel = kwargs.get('sequel')
        self.__prequel = kwargs.get('prequel')
        self.__score = kwargs.get('score')
        self.__nsfw = kwargs.get('nsfw')
        self.__recommendations = kwargs.get('recommendations')

    @property
    def id(self) -> int:
        return self.__id

    @property
    def anilist_id(self) -> int:
        return self.__anilist_id

    @property
    def mal_id(self) -> int:
        return self.__mal_id

    @property
    def tmdb_id(self) -> int:
        return self.__tmdb_id

    @property
    def format(self) -> str:
        return self.__format

    @property
    def status(self) -> str:
        return self.__status

    @property
    def titles(self) -> dict:
        return self.__titles

    @property
    def description(self) -> str:
        return self.__description

    @property
    def start_date(self) -> str:
        return self.__start_date

    @property
    def end_date(self) -> str:
        return self.__end_date

    @property
    def weakly_airing_day(self) -> str:
        return self.__weakly_airing_day

    @property
    def season_period(self) -> str:
        return self.__season_period

    @property
    def season_year(self) -> str:
        return self.__season_year

    @property
    def episodes_count(self) -> int:
        return self.__episodes_count

    @property
    def episodes_duration(self) -> int:
        return self.__episodes_duration

    @property
    def trailer_url(self) -> str:
        return self.__trailer_url

    @property
    def cover_image(self) -> str:
        return self.__cover_image

    @property
    def has_cover_image(self) -> bool:
        return self.__has_cover_image

    @property
    def cover_color(self) -> str:
        return self.__cover_color

    @property
    def banner_image(self) -> str:
        return self.__banner_image

    @property
    def genres(self) -> list:
        return self.__genres

    @property
    def sagas(self) -> list:
        return self.__sagas

    @property
    def sequel(self) -> int:
        return self.__sequel

    @property
    def prequel(self) -> int:
        return self.__prequel

    @property
    def score(self) -> float:
        return self.__score

    @property
    def nsfw(self) -> bool:
        return self.__nsfw

    @property
    def recommendations(self) -> list:
        return self.__recommendations

    def __repr__(self) -> str:
        return f'<id={self.id} title={list(self.__titles.values())[0]!r} nsfw={self.__nsfw}>'


class SongObj:
    def __init__(self, **kwargs):
        self.__id = kwargs.get('id')
        self.__anime_id = kwargs.get('anime_id')
        self.__title = kwargs.get('title')
        self.__artist = kwargs.get('artist')
        self.__album = kwargs.get('album')
        self.__year = kwargs.get('year')
        self.__season = kwargs.get('season')
        self.__duration = kwargs.get('duration')
        self.__preview_url = kwargs.get('preview_url')
        self.__open_spotify_url = kwargs.get('open_spotify_url')
        self.__local_spotify_url = kwargs.get('local_spotify_url')
        self.__type = kwargs.get('type')

    @property
    def id(self) -> int:
        return self.__id

    @property
    def anime_id(self) -> int:
        return self.__anime_id

    @property
    def title(self) -> str:
        return self.__title

    @property
    def artist(self) -> str:
        return self.__artist

    @property
    def album(self) -> str:
        return self.__album

    @property
    def year(self) -> int:
        return self.__year

    @property
    def season(self) -> str:
        return self.__season

    @property
    def duration(self) -> int:
        return self.__duration

    @property
    def preview_url(self) -> str:
        return self.__preview_url

    @property
    def open_spotify_url(self) -> str:
        return self.__open_spotify_url

    @property
    def local_spotify_url(self) -> str:
        return self.__local_spotify_url

    @property
    def type(self) -> str:
        return self.__type

    def __repr__(self) -> str:
        return f'<id={self.id} title={self.title!r} artist={self.artist!r}>'


class AuthMeObj:
    def __init__(self, **kwargs):
        self.__username = kwargs.pop('username')
        self.__email = kwargs.pop('email')
        self.__email_verified = kwargs.pop('email_verified')
        self.__role = kwargs.pop('role')
        self.__gender = kwargs.pop('gender')
        self.__avatar_tracker = kwargs.pop('avatar_tracker')
        self.__localization = kwargs.pop('localization')
        self.__has_anilist = kwargs.pop('has_anilist')
        self.__has_mal = kwargs.pop('has_mal')
        self.__id = kwargs.pop('id')

    @property
    def username(self) -> str:
        return self.__username

    @property
    def email(self) -> str:
        return self.__email

    @property
    def email_verified(self) -> bool:
        return self.__email_verified

    @property
    def role(self) -> str:
        return self.__role

    @property
    def gender(self) -> int:
        return self.__gender

    @property
    def avatar_tracker(self) -> str:
        return self.__avatar_tracker

    @property
    def localization(self) -> str:
        return self.__localization

    @property
    def has_anilist(self) -> bool:
        return self.__has_anilist

    @property
    def has_mal(self) -> bool:
        return self.__has_mal

    @property
    def id(self) -> int:
        return self.__id

    def __repr__(self) -> str:
        return f'<id={self.id} username={self.username!r} email_verified={self.email_verified}>'
