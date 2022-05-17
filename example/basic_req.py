# The first thing is to import the Library
from objects import DataObj
from wrapper import AniApi

if __name__ == '__main__':
    # Create the Client instance to use the API.
    client = AniApi()
    # When you now wonder, 'But why, where is the JWT token?' Well, for basic requests
    # you don't need a token.

    # Here we want to get the list of all the anime. We also don't want all other information like the response
    # code, the headers, the status code, etc.
    animes: DataObj = client.get_anime(year=2000, page=50).data

    # Print all animes  that are nsfw and on page 3

    # for anime in animes.documents:
    #     if anime.nsfw:
    #         print(anime)
