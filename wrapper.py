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

from utils import AnimeGenres

from config import API_TOKEN

conn = http.client.HTTPSConnection("api.aniapi.com")

headers = {
    'Authorization': f'Bearer {API_TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}


class AniApi(http.client.HTTPSConnection):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)

        self.headers = {
            'Authorization': f'Bearer {kwargs.pop("token")}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def get_anime(self, url, body=None) -> str:
        self.request('GET', url, body, self.headers)

        res = self.getresponse()
        data = res.read()
        return data.decode('utf-8')


if __name__ == '__main__':
    print(AnimeGenres.ANIMALS.value)
    pass
    # api = AniApi('api.aniapi.com', token=API_TOKEN)
    #
    # res = api.get_anime('/v1/anime')
    # print(res)
