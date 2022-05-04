#!/bin/python3
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

import time
from urllib.parse import urlencode

from _types.context import Context
from config import API_TOKEN
from connection import ApiConnection
from constants import API_VERSION, DEFAULT_HEADER
from dataproc import create_data_dict
from objectcreator import AnimeObj, DataObj, EpisodeObj, SongObj
from objectcreator import Context as Ctx
from utils import (InvalidParamsException,
                   ANIME_REQ,
                   EPISODE_REQ,
                   SONG_REQ,
                   InvalidParamsValueException)


class AniApi(ApiConnection):
    def __init__(self, token: str = ''):
        """ This is the Base Class for the AniApi wrapper.

        Attributes:
        -----------
        token : [:class:`str`]
            The API Token you get from https://aniapi.com/profile.
            You will only need this token when you want to use things from outer scope than the `GET` methods.

        timeout : [:class:`int`]
            The timeout for the connection.
        """

        super().__init__()

        # Define default headers with token
        self.headers = DEFAULT_HEADER(token)

    def get_requests(self, _id, url, params, obj) -> dict:
        """ For development method. this method will be used later to make it easier to implement new endpoints.

        Parameters
        ----------
        _id : [:class:`int`]
            The id for the url for a specific endpoint e.s. `/anime/{id}`.
        url : [:class:`str`]
            The url identifier for the endpoint e.s. `anime`.
        params : [:class:`dict`]
            The extra filter arguments to deliver
        obj : [:class:`object`]
            The object for the conversion

        Returns
        -------
        :class:`dict`
            The converted response

        """
        res, headers = self.get(f'/{API_VERSION}/{url}/{_id}?{urlencode(params)}', headers=self.headers)
        data = create_data_dict(res, headers)

        if _id:
            data['data'] = obj(**data.get('data'))
            return data

        if data.get('data', False):
            data['data']['documents'] = [obj(**i) for i in data['data']['documents']]
            data['data'] = DataObj(**data['data'])

        return data

    # Here comes all the Anime related methods.
    def get_anime(self, anime_id: int = '', **kwargs) -> Ctx:
        """ Get an Anime object list from the API.
        You can provide an ID or query parameters to get a single AnimeObject (:class:`Anime`) or an :class:`list`
        of objects.

        Parameters:
        ----------
        anime_id : Optional[:class:`int`]
            The ID for the Anime you want to get. Beware it's **not** the mal_id, tmdb_id or the anilist_id they
            can be different and getting handeld by the `**kwargs` parameter. When you provide an ID, you can't use the
            `**kwargs` parameter.

        **kwargs : Optional[:class:`dict`]
            The parameters that you want to use to spice up your request.
            Supported Parameters can be found inside the `utils.flags` file.

        Returns
        -------
        Context
            A Context object with the query returns and the rate limit information.

        Raises
        -------
        InvalidFlagsException
            When you try to use any flags that are not supported.

        Examples
        ---------
        >>> from wrapper import AniApi
        >>> api = AniApi(token='your_token')
        >>> api.get_anime(1, status=0)  # Get Anime with ID 1 and status 0 (finished)
        <status_code=200 message='Anime found' data=<id=1 title='Cowboy Bebop' episodes=26 status=0> version='1'>
        """

        invalid = set(kwargs) - set(ANIME_REQ)

        if invalid:
            raise InvalidParamsException(f'Invalid parameters: {invalid}')

        data = self.get_requests(anime_id, 'anime', kwargs, AnimeObj)

        return Ctx(**data)

    def get_random_anime(self, count: int = 1, nsfw: bool = False) -> Ctx:
        """ Get one or more random Animes from the API.

        Parameters
        ----------
        count : :class:`int`
            The amount of Animes you want to get. Value should be between 1 and 50.

        nsfw : :class:`bool`
            If you want to get NSFW Animes. Default is False.

        Returns
        -------
        :class:`Ctx`
            Context object with the query returns and the rate limit information.

        Raises
        -------
        ValueError
            The count can't be less than 1 or more than 50. The api return 50 at max.

        """
        if count > 50 or count < 1:
            raise ValueError('Count must be less than 50 and more or equal to 1')

        res, header = self.get(f'/{API_VERSION}/random/anime/{count}/{nsfw}', headers=self.headers)
        data = create_data_dict(res, header)

        data['data'] = [AnimeObj(**anime) for anime in data['data']]
        return Ctx(**data)

    # Here comes all the Episode related methods.
    def get_episode(self, episode_id: int = '', **kwargs) -> Ctx:
        """ Get an Episode from the API.

        Parameters
        ----------
        episode_id : Optional[:class:`int`]
            Give an ID to get a Specific Episode, note that all other parameters get dumped when you provide an ID.

        **kwargs :
            Apply filter like `anime_id` or enter a `pagination` valid filter can be found inside the `utils.flags` file.

        Returns
        -------
        :class:`Ctx`
            A context object with the query returns and the rate limit information.
        Raises
        -------
        InvalidFlagsException

        Examples
        ---------
        >>> from wrapper import AniApi
        >>> api = AniApi(token='your_token')
        >>> api.get_episode(1)  # Get Episode with ID 1
        <status_code=200 message='Episode found' data=<id=1 anime_id=1 number=1 locale=en> version='1'>
        """

        invalid = set(kwargs) - set(EPISODE_REQ)

        if invalid:
            raise InvalidParamsValueException(f'Invalid parameters: {invalid}')

        data = self.get_requests(episode_id, 'episode', kwargs, EpisodeObj)
        return Ctx(**data)

    # Here are the song related methods.
    def get_song(self, song_id: int = '', **kwargs) -> Ctx:
        """ Get from 1 up to 100 songs at the time from the Api

        Parameters
        ----------
        song_id : Optional[:class:`int`]
            Give an ID to get a Specific Song, note that all other parameters get dumped when you provide an ID.

        kwargs : Optional[:class:`dict`]
            Apply filter like `anime_id` or enter a `pagination` valid filter can be found inside the `utils.flags` file
            or at the docs: https://aniapi.com/docs/resources/song#parameters-1

        Returns
        -------
        :class:`Ctx`
            A context object with the query returns and the rate limit information.

        """
        invalid = set(kwargs) - set(SONG_REQ)

        if invalid:
            raise InvalidParamsException(f'Invalid parameters: {invalid}')

        data = self.get_requests(song_id, 'song', kwargs, SongObj)
        return Ctx(**data)

    def get_random_song(self, count: int = 1) -> Ctx:
        """
        It's the same as get_random_anime but for another endpoint and without nsfw tag.

        Parameters
        ----------
        count : :class:`int`
            The amount of songs you want to get. Value should be between 1 and 50.
            When you go over the value you get 50 at max. so I set a cap at 50.

        Returns
        -------
        :class:`Ctx`
            Context object with the query returns and the rate limit information.

        """
        if count > 50 or count < 1:
            raise ValueError('Count must be less than 50 and more or equal to 1')

        res, header = self.get(f'/{API_VERSION}/random/song/{count}', headers=self.headers)
        data = create_data_dict(res, header)

        data['data'] = [SongObj(**song) for song in data['data']]
        return Ctx(**data)


if __name__ == '__main__':
    test = False
    start = time.time()

    client = AniApi(token=API_TOKEN)

    if not test:
        _data: Ctx = client.get_song(page=2, per_page=2)
        print(_data)
    else:
        f = 20
        time_list = ()

        for f in range(f):  # FOR PERFORMANCE TESTING
            start_time = time.time()
            _data = client.get_song()
            time_list += (time.time() - start_time,)
            # print(_data)

        print(f'{sum(time_list) / f:.3f}s')

    end = time.time()

    print(f'Time: {(end - start):.3f}s')
    # print(client.get_anime(_id=1))
