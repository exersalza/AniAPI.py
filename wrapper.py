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

from utils import enums
from utils.errors import CustomErrors
from type.anime import Anime

from config import API_TOKEN


class AniApi(http.client.HTTPSConnection):
    def __init__(self, token: str):
        super().__init__(host='api.aniapi.com')

        self.headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def get_anime(self, _id=None) -> dict:
        """
        Get an Anime list or when you provide an ID it will give you the Anime with the related ID.

        :param _id: ID of the Anime
        :return: Dictionary with the response
        """
        self.request('GET', f'/v1/anime/{_id if _id else ""}', headers=self.headers)

        res = self.getresponse()
        data = res.read()
        return json.loads(data.decode('utf-8'))

    def get_random_anime(self, count: int, nsfw: bool = False) -> dict:
        self.request('GET', f'/v1/random/anime/{count}/{nsfw}', headers=self.headers)

        response = self.getresponse()
        data = response.read()
        return json.loads(data.decode('utf-8'))


if __name__ == '__main__':
    client = AniApi(token=API_TOKEN)
    pprint.pprint(client.get_anime(-1))
