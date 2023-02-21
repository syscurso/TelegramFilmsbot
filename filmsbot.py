# https://www.themoviedb.org
# https://www.themoviedb.org/documentation/api/discover
# https://api.telegram.org/
# https://api.themoviedb.org/3/movie/upcoming?with_genres=35&api_key=7be72508776961f3948639fbd796bccd&language=es

import requests

import json


def filmsBot(filmsToShow, type, gener, language):
    # Si este token api_key caduca tenéis que conseguir uno vosotros en la página como muestro al final del video.
    api_key = '7be72508776961f3948639fbd796bccd'
    page = f'https://api.themoviedb.org/3/movie/{type}?with_genres={gener}&api_key={api_key}&language={language}'
    api = requests.get(page)
    json_data = json.loads(api.content)


    for n in range(filmsToShow):

        title = json_data['results'][n]['title']
        votes = json_data['results'][n]['vote_average']
        description = json_data['results'][n]['overview']

        message = f'Titulo: {title}\n Votes: {votes}\n Sinopsis: {description}'
        #Aquí tenéis que poner vuestro propio Token de Telegram
        requests.post('https://api.telegram.org/bot6137218457:AAHfyAdwgojRjurZUFcSVPemDIlMvYKOCDk/sendMessage',
              data = {'chat_id' : '-1001713618434', 'text' : message})

# Tipo Popular o upcoming
# Genero 35 es comedia Genero 18 es Drama

filmsBot(5, 'popular', '18', 'es')
