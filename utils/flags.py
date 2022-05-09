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

# for more information look at: https://aniapi.com/docs/pagination
PAGINATION = ['page',
              'locale',
              'per_page',
              'ids',
              'sort_fields',
              'sort_directions']

ANIME_REQ = ['title',
             'anilist_id',
             'mal_id',
             'tmdb_id',
             'formats',
             'status',
             'year',
             'season',
             'genres',
             'nsfw',
             'with_episodes'] + PAGINATION

EPISODE_REQ = ['anime_id',
               'number',
               'is_dub',
               'locale'] + PAGINATION

SONG_REQ = ['anime_id',
            'title',
            'artist',
            'year',
            'season',
            'type'] + PAGINATION

USER_REQ = ['username',
            'email'] + PAGINATION

UPDATE_USER_REQ = ['password',
                   'localization',
                   'anilist_id',
                   'anilist_token']
