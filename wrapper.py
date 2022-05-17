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

from urllib.parse import urlencode

from connection import ApiConnection
from constants import API_VERSION, default_header
from dataproc import create_data_dict
from objects import AnimeObj, DataObj, EpisodeObj, SongObj, UserSObj, UserBObj
from objects import Context as Ctx
from utils import (InvalidParamsException,
                   ANIME_REQ,
                   EPISODE_REQ,
                   SONG_REQ,
                   InvalidParamsValueException, UPDATE_USER_REQ, USER_REQ, USER_STORY_REQ)


# Todo:
# - remove isinstance checks and replace it with status code checks thx


class AniApi(ApiConnection):
    def __init__(self, token: str = ''):
        """ This is the Base Class for the AniApi wrapper.
        This class will only contain the resources given at the docs,
        oauth will be extended by the other classes.

        In this class you will find other than the standard requests the
        `auth me` requests, when you want them oAuth stuff please use the
        :class:`AniApiOAuth` class, it's a subclass of this class.

        Attributes:
        -----------
        token : [:class:`str`]
            The API Token you get from https://aniapi.com/profile.
            If your application is inside the read-only scope then you
            don't need to provide a token.

        timeout : [:class:`int`]
            The timeout for the connection.
        """

        super().__init__()

        # Define default headers with token
        self.headers = default_header(token)

    def get_requests(self, _id, url, params, obj) -> dict:
        """ For development method. this method will be used later to
        make it easier to implement new endpoints.

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

        if data.get('status_code', 404) != 200:
            return data
        
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
        You can provide an ID or query parameters to get a
        single AnimeObject (:class:`Anime`) or an :class:`list`
        of objects.

        Parameters:
        ----------
        anime_id : Optional[:class:`int`]
            The ID for the Anime you want to get. Beware it's **not** the mal_id,
            tmdb_id or the anilist_id they
            can be different and getting handeld by the `**kwargs` parameter.
            When you provide an ID, you can't use the
            `**kwargs` parameter.

        **kwargs : Optional[:class:`dict`]
            The parameters that you want to use to spice up your request.
            Supported Parameters can be found inside the `utils.flags` file.

        Returns
        -------
        :class:`Ctx`
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

        if data.get('status_code', 404) != 200:
            return Ctx(**data)

        data['data'] = [AnimeObj(**anime) for anime in data['data']]
        return Ctx(**data)

    # Here comes all the Episode related methods.
    def get_episode(self, episode_id: int = '', **kwargs) -> Ctx:
        """ Get an Episode from the API.

        Parameters
        ----------
        episode_id : Optional[:class:`int`]
            Give an ID to get a Specific Episode, note that all other
            parameters get dumped when you provide an ID.

        **kwargs :
            Apply filter like `anime_id` or enter a `pagination` valid filter
            can be found inside the `utils.flags` file.

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
            Give an ID to get a Specific Song, note that all other parameters
            get dumped when you provide an ID.

        kwargs : Optional[:class:`dict`]
            Apply filter like `anime_id` or enter a `pagination` valid filter can
            be found inside the `utils.flags` file
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

        # This is just for that the user don't bring a number that is bigger/lower than
        # the api can handle it
        if count > 50 or count < 1:
            raise ValueError('Count must be less than 50 and greater or equal to 1')

        res, header = self.get(f'/{API_VERSION}/random/song/{count}', headers=self.headers)
        data = create_data_dict(res, header)

        if data.get('status_code', 404) != 200:
            return Ctx(**data)

        data['data'] = [SongObj(**song) for song in data['data']]
        return Ctx(**data)

    # Resource requests
    def get_resources(self, version: float, _type: int) -> Ctx:
        """ Get the resources of the AniApi

        Parameters
        ----------
        version : :class:`float`
            The version from the resource.

        _type : :class:`int`
            The type of resource you want to get.
            0 = Anime Genres,
            1 = Locales

        Returns
        -------
        :class:`Ctx`
            A context object with the query returns and the rate limit information.
        """

        res, header = self.get(f'/{API_VERSION}/resources/{version}/{_type}', headers=self.headers)
        data = create_data_dict(res, header)
        return Ctx(**data)

    # User Story's
    def get_user_story(self, story_id: int = '', **kwargs) -> Ctx:
        """ Get a list or specific UserStory from the API

        Parameters
        ----------
        story_id : [:class:`int`]
            The UserStory id to get, note: when you provide an id.

        kwargs
            Include filter for the List request

        Returns
        -------
        :class:`Ctx`
            Ctx object with the response from the get request

        """

        invalid = set(kwargs) - set(USER_STORY_REQ)

        if invalid:
            raise InvalidParamsException(f'Invalid arguments: {invalid}')

        res, header = self.get(f'/{API_VERSION}/user_story/{story_id}?{urlencode(kwargs)}', self.headers)
        data = create_data_dict(res, header)
        return Ctx(**data)

    def create_user_story(self, user_id: int, anime_id: int, status: int, **kwargs) -> Ctx:
        """ This will create a UserStory based on the given parameters.

        Parameters
        ----------
        user_id : :class:`int`
            The User ID for the UserStory's bind.

        anime_id : :class:`int`
            The UserStory's Anime ID.

        status : :class:`int`
            The UserStory's watching status.

        kwargs : Optional
            These are the optional parameters.

            current_episode (int) -> The current watching progress. It must be less than
            the Anime's episode_count value, when you provide a status equal to 1 or 2 this field is auto-calculated.

            current_episode_ticks (int) -> The current episode watching time in milliseconds.

        Returns
        -------
        :class:`Ctx`
            The response as Ctx object
        """

        invalid = set(kwargs) - {'current_episode',
                                 'current_episode_ticks'}

        if invalid:
            raise InvalidParamsException(f'Invalid parameters given: {invalid}')

        udata = {'user_id': user_id, 'anime_id': anime_id, 'status': status}
        udata.update(kwargs)

        res, header = self.post(url=f'/{API_VERSION}/user_story/', headers=self.headers, data=udata)
        data = create_data_dict(res, header)

        return Ctx(**data)

    def update_user_story(self, story_id: int, user_id: int, anime_id: int, status: int, ce: int, cet: int) -> Ctx:
        """
        Update a UserStory

        Parameters
        ----------
        story_id : [:class:`int`]
            -> id, on the docs.
            The UserStory's unique identifier.

        user_id : [:class:`int`]
            -> user_id, on the docs.
            The userid that is related to the UserStory.

        anime_id : [:class:`int`]
            -> anime_id, on the docs
            The UserStory's anime id.

        status : [:class:`int`]
            -> status, on the docs
            The watching status of the UserStory.

        ce : [:class:`int`]
            -> current_episode, on the docs
            The current watching progress on the UserStory, note: the watching progress must be less or equal to the
            anime's `episode_count`.

        cet : [:class:`int`]
            -> current_episode_ticks, on the docs
            The UserStory's `current_episode` watching time in milliseconds.

        Returns
        -------
        :class:`Ctx`
            A response from the API to prove if it works or not.
        """

        udata = {'id': story_id, 'user_id': user_id, 'anime_id': anime_id,
                 'status': status, 'current_episode': ce, 'current_episode_ticks': cet}

        res, header = self.post(url=f'/{API_VERSION}/user_story', headers=self.headers, data=udata)
        data = create_data_dict(res, header)

        return Ctx(**data)

    def delete_user_story(self, _id: int) -> Ctx:
        """
        Deletes a UserStory on the provided unique identifier.

        Parameters
        ----------
        _id : [:class:`int`]
            The id from the UserStory that wanted to be deleted.

        Returns
        -------
        :class:`Ctx`
            Context obj with the response inside it

        Notes
        -----
        You should only use the endpoint when the User has 0 linked trackers, otherwise it will get re-imported.

        """

        res, header = self.delete(url=f'/{API_VERSION}/user_story/{_id}', headers=self.headers)
        data = create_data_dict(res, header)

        return Ctx(**data)

    # User related stuff
    def get_user(self, user_id: int = '', **kwargs) -> Ctx:
        """
        Get user list of users or when you provide a user_id to get a specific user

        Parameters
        ----------
        user_id : [:class:`int`]
            A UserID for specified search of user.

        kwargs
            Bring up pagination or currently two arguments for filtering:

            username: is not case-sensitive, it searches for substrings in the username.
            email: it's the same as username.

        Returns
        -------
        :class:`ctx`
            Context object with the query results
        """

        invalid = set(kwargs) - set(USER_REQ)

        if invalid:
            raise InvalidParamsException(f'Invalid parameters: {invalid}')

        data = self.get_requests(user_id, 'user', kwargs, UserSObj)
        return Ctx(**data)

    def update_user(self, user_id: int, gender: int, **kwargs) -> Ctx:
        """ This method will update user information, please read the notes.

        Parameters
        ----------
        user_id : [:class:`int`]
            The unique identifier for the user that you want to edit.

        gender : [:class:`int`]
            The gender of the user that will be changed or not.

        kwargs
            Other settings to change on the user's acc, lists can be found at
            `utils.flags.UPDATE_USER_REQ` or at the docs at:
            https://aniapi.com/docs/resources/user#parameters-2

        Returns
        -------
        :class:`Ctx`
            A Ctx object with the return object

        Notes
        -----
        **It is NOT Recommended that you implement such function or form,
        when you want to do so, please redirect the
        User to the website. More information about it on the docs:
        https://aniapi.com/docs/resource/user#update-an-user**
        """

        invalid = set(kwargs) - set(UPDATE_USER_REQ)

        if invalid:
            raise InvalidParamsException(f'Invalid parameters: {invalid}')

        res, header = self.post(f'/{API_VERSION}/user', headers=self.headers, data={'id': user_id,
                                                                                    'gender': gender,
                                                                                    **kwargs})
        data = create_data_dict(res, header)

        return Ctx(**data)

    def delete_user(self, _id: int) -> Ctx:
        """
        This method will delete the user with the given id.
        Parameters
        ----------
        _id : [:class:`int`]
            The unique identifier for the user that you want to delete.

        Returns
        -------
        :class:`Ctx`
            A Ctx object with the return object
        """

        res, header = self.delete(f'/{API_VERSION}/user/{_id}', headers=self.headers)
        data = create_data_dict(res, header)
        return Ctx(**data)

    # Auth me.
    def auth_me(self, jwt: str) -> Ctx:
        """
        This method will test the given token and return the user
        information (if it exists and its valid).

        Parameters
        ----------
        jwt : :class:`str`
            The JWT token to test.

        Returns
        -------
        :class:`Ctx`
            A context object with the response. If the token is invalid you
            will get a status code of 401.
        """

        res, header = self.get(f'/{API_VERSION}/auth/me', headers=default_header(jwt))
        data = create_data_dict(res, header)

        # Just checking for the status code, so it will hopefully not crash the
        # program when it throws something other than 200 :)
        if data.get('status_code', 404) != 200:
            return Ctx(**data)

        data['data'] = UserBObj(**data.get('data'))
        return Ctx(**data)
