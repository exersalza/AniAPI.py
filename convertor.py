from _types import anime, context, data


class AnimeObj(anime.Anime):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f'<id={self.id} title={(list(self.titles.values())[0])!r} episodes={self.episodes_count} status={self.status}>'


class ContextObj(context.Context):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f'<status_code={self.status_code} message={self.message!r} version={self.version} data={self.data}>'


class DataObj(data.Data):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f'{self.__dict__}'
