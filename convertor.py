from config import API_TOKEN
from type.anime import Anime
from wrapper import AniApi


class Dict2Obj(Anime):
    def __init__(self, **dict_):
        self.__dict__ = dict_

    def __repr__(self):
        return str(self.__dict__)


if __name__ == '__main__':
    api = AniApi(token=API_TOKEN)
    d = api.get_anime(1).get('data')
    print(d)
    d2o: Anime = Dict2Obj(**d)
    print(d2o.titles)
