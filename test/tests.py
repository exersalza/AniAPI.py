import time

from wrapper import AniApi
from config import API_TOKEN


if __name__ == '__main__':
    test = False
    start = time.time()

    client = AniApi(token=API_TOKEN)

    if not test:
        _data = client.get_user_story()

        print(_data)
    else:
        f = 20
        time_list = ()

        for f in range(f):  # FOR PERFORMANCE TESTING
            start_time = time.time()
            _data = client.get_resources(1.0, 1)
            time_list += (time.time() - start_time,)

        print(f'{sum(time_list) / f:.3f}s')

    end = time.time()

    print(f'Time: {(end - start):.3f}s')
