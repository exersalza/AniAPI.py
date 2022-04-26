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

import http.client
import json
import pprint
import time

from urllib.parse import urlencode
from typing import Union, List

from _types.anime import Anime
from _types.context import Context

from config import API_TOKEN
from connection import ApiConnection
from objectcreator import AnimeObj, DataObj, RateLimit
from utils import InvalidParamsException, ANIME_REQ
from constants import API_VERSION, DEFAULT_HEADER

from context import Context as ctx


def get_ratelimit(res: dict) -> RateLimit:
    """
    Extract the rate limit from the response.

    Parameters
    ----------
    res : [:class:`http.client.HTTPResponse`]
        The response from the API.

    Returns
    -------
    :class:`RateLimit`
    """
    return RateLimit(limit=res.get('X-RateLimit-Limit'),
                     remaining=res.get('X-RateLimit-Remaining'),
                     reset=res.get('X-RateLimit-Reset'))


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

    # Here comes all the Anime related methods.
    def get_anime(self, _id=None, **kwargs) -> ctx:
        r""" Get an Anime object list from the API.
        You can provide an ID or query parameters to get a single AnimeObject (:class:`Anime`) or an :class:`list` of objects.

        Parameters:
        ----------
        _id : Optional[:class:`int`]
            The ID for the Anime you want to get. Beware it's **not** the mal_id, tmdb_id or the anilist_id they
            can be different and getting handeld by the `**kwargs` parameter.

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

        res, header = self.get(f'/{API_VERSION}/anime/{_id if _id else ""}?{urlencode(kwargs)}', headers=self.headers)
        data = json.loads(res.decode('utf-8'))

        data['ratelimit'] = get_ratelimit(header)
        if _id is not None:
            data['data'] = AnimeObj(**data['data'])
            return ctx(**data)

        data['data']['documents'] = [AnimeObj(**anime) for anime in data['data']['documents']]
        data['data'] = DataObj(**data['data'])
        return ctx(**data)

    def get_random_anime(self, count: int = 1, nsfw: bool = False) -> ctx:
        """ Get one or more random Animes from the API.

        Parameters
        ----------
        count : :class:`int`
            The amount of Animes you want to get. Value should be between 1 and 50.

        nsfw : :class:`bool`
            If you want to get NSFW Animes. Default is False.

        Returns
        -------
        :class:`ctx`
            Context object with the query returns and the rate limit information.

        Raises
        -------
        ValueError
            The count can't be less than 1 or more than 50. The api return 50 at max.

        """
        if 1 > count < 50:
            raise ValueError('Count must be less than 50 and more or equal to 1')

        res, header = self.get(f'/{API_VERSION}/random/anime/{count}/{nsfw}', headers=self.headers)

        data = json.loads(res.decode('utf-8'))
        data['ratelimit'] = get_ratelimit(header)
        data['data'] = [AnimeObj(**anime) for anime in data['data']]
        return ctx(**data)

    # Here comes all the Episode related methods.
    def get_episode(self, _id=None) -> ctx:
        """
        Get an Episode with the related ID.

        :param _id: ID of the Episode
        :return: Dictionary with the response
        """

        self.request('GET', f'/{API_VERSION}/episode/{_id if _id else ""}', headers=self.headers)

        res = self.getresponse()
        return json.loads(res.read().decode('utf-8'))


if __name__ == '__main__':
    test = False
    start = time.time()

    client = AniApi(token=API_TOKEN)

    if not test:
        data: ctx = client.get_random_anime(1)
        print(data)
    else:
        f = 0
        time_list = []

        for f in range(10):  # FOR PERFORMANCE TESTING
            start_time = time.time()
            client.get_anime()
            time_list.append(time.time() - start_time)

        print(f'{sum(time_list) / 10:.2f}')

    end = time.time()

    print(f'Time: {(end - start):.2f}s')
    # print(client.get_anime(_id=1))
