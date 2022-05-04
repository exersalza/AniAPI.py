import json

from objectcreator import RateLimit


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
