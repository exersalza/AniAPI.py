from _types.anime import Anime


class Dict2AnimeObj(Anime):
    def __init__(self, **dict_):
        self.__dict__ = dict_

    def __repr__(self):
        return f'<id={self.id} title={(list(self.titles.values())[0])!r} episodes={self.episodes_count} status={self.status}>'
