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
from http.client import HTTPSConnection, HTTPMessage
from typing import Tuple


class ApiConnection(HTTPSConnection):
    def __init__(self):
        """
        This is the Base connection class for the AniApi wrapper.
        """

        super().__init__(host='api.aniapi.com')

    def get(self, url: str, headers: dict) -> Tuple[bytes, HTTPMessage]:
        """ This will send a `GET` request to aniapi.com

        Parameters
        ----------
        url : :class:`str`
            The url to send the request to.

        headers : :class:`dict`
            The headers to send with the request. This is for the jwt token and to tell the API what we want back from them.
        Returns
        -------
        :class:`bytes`
            The read response from the server.
        Notes
        -----
        The JWT token is momentary not used, but maybe it will be later, so I left it in.
        """

        self.connect()

        self.request('GET', url, headers=headers)
        r = self.getresponse()
        res = r.read()
        header = r.headers

        self.close()
        return res, header
