import requests


def get_movie(title=None, year=None, imdb_id=None):
    url = 'http://www.omdbapi.com/'
    params = {'plot': 'short', 'r': 'json'}
    if title is not None:
        params['t'] = title
    if year is not None:
        params['y'] = year
    if imdb_id is not None:
        params['i'] = imdb_id

    response = requests.get(url, params=params)
    if not response.ok:
        # api was not available
        return None
    resp = response.json()

    if resp['Response'] == 'True':
        return {
            'language': resp['Language'],
            'director': resp['Director'],
            'rated': resp['Rated'],
            'title': resp['Title'],
            'year': resp['Year'],
            'imdb_id': resp['imdbID'],
            'imdb_rating': resp['imdbRating']}
    else:
        # movies was not found.
        return None


def get_movie_by_title(title=None, year=None):
    """Sends a request to omdbapi to get movie data.

    If there is a problem with connection returns None.
    """
    return get_movie(title=title, year=year)


def get_movie_by_id(imdb_id):
    """Sends a request to omdbapi to get movie data.

    If there is a problem with connection returns None.
    """
    return get_movie(imdb_id=imdb_id)
