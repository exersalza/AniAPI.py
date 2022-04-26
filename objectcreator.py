from _types import anime, context, data, ratelimit


class AnimeObj:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f'<id={self.id} title={(list(self.titles.values())[0])!r} episodes={self.episodes_count} status={self.status}>'


class DataObj:
    def __init__(self, **kwargs):
        self.current_page = kwargs.get('current_page')
        self.count = kwargs.get('count')
        self.documents = kwargs.get('documents')
        self.last_page = kwargs.get('last_page')

    def __repr__(self):
        return f'<current_page={self.current_page} count={self.count} documents={self.documents[:3]} last_page={self.last_page}>'


class RateLimit:
    def __init__(self, limit: str, remaining: str, reset: str):
        self.limit = limit
        self.remaining = remaining
        self.reset = reset

    def __repr__(self):
        return f'<limit={self.limit} remaining={self.remaining} reset={self.reset}>'
