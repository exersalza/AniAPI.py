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

import json

from objects import RateLimit


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


def create_data_dict(res: bytes, header: dict) -> dict:
    """
    Creates a data dictionary from the response.
    Parameters
    ----------
    res : [:class:`bytes`]
        The raw response from the API.

    header : [:class:`dict`]
      Enter the header from the `get` method.

    Returns
    -------
    :class:`dict`
        The data dictionary.
    """
    data: dict = json.loads(res.decode('utf-8'))
    data['ratelimit'] = get_ratelimit(header)
    return data
