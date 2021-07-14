import requests, json
from .exceptions import IMDBConnectionError, IMDBException
from django.conf import settings


def get_imdb_id(title, api_key=None, lang=None):
    api_key = api_key or settings.IMDB_API_KEY
    lang = lang or settings.API_LANG

    response = requests.get(f'https://imdb-api.com/{lang}/API/SearchMovie/{api_key}/{title}')

    if response.status_code != 200 :
        raise IMDBConnectionError

    film_data = json.loads(response.text)

    error_message = film_data['errorMessage']
    if error_message != '':
        raise IMDBException(error_message)
    
    imdb_film_id = film_data['results'][0]['id']

    return imdb_film_id


def get_imdb_rating(imdb_id, api_key=None, lang=None):
    api_key = api_key or settings.IMDB_API_KEY
    lang = lang or settings.API_LANG
        
    response = requests.get(f'https://imdb-api.com/{lang}/API/Ratings/{api_key}/{imdb_id}')

    if response.status_code != 200:
        raise IMDBConnectionError

    ratings_data = json.loads(response.text)

    error_message = ratings_data['errorMessage']
    if error_message != '':
        raise IMDBException(error_message)

    imdb_film_rating = ratings_data['imDb']

    return imdb_film_rating
