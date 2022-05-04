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
