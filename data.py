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
from typing import Optional, List

from _types.anime import Anime


class AnimeListData:
    def __init__(self, **kwargs):
        self.__current_page = kwargs.get('current_page')
        self.__count = kwargs.get('count')
        self.__documents = kwargs.get('documents')
        self.__last_page = kwargs.get('last_page')

    @property
    def current_page(self) -> int:
        return self.__current_page

    @property
    def count(self) -> int:
        return self.__count

    @property
    def documents(self) -> List[Anime]:
        return self.__documents

    @property
    def last_page(self) -> int:
        return self.__last_page

    def __repr__(self):
        return f'<current_page={self.__current_page} count={self.__count} last_page={self.__last_page}>'


