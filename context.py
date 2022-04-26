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
from typing import List, Union, Any

from _types.ratelimit import RateLimit


class Context:
    def __init__(self, **kwargs):  # Create a Non-changeable object
        self.__status_code = kwargs.get('status_code', 404)
        self.__message = kwargs.get('message', 'Not Found')
        self.__data = kwargs.get('data', {})
        self.__version = kwargs.get('version', '1')
        self.__ratelimit = kwargs.get('ratelimit', None)

    @property
    def status_code(self) -> int:
        return self.__status_code

    @property
    def message(self) -> str:
        return f'{self.__message!r}'

    @property
    def data(self) -> Union[Any, List[Any]]:
        return self.__data

    @property
    def version(self) -> str:
        return self.__version

    @property
    def ratelimit(self) -> RateLimit:
        return self.__ratelimit

    def __repr__(self):
        return f'<status_code={self.__status_code} message={self.__message!r} data={self.__data} version={self.__version!r}>'

