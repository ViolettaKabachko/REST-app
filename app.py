from flask import Flask, request, jsonify
from flask_cors import CORS
from random import choice

categories = ['action',
              'rpg',
              'adventure',
              'simulation',
              'sports_and_racing']

app = Flask(__name__)
CORS(app)

responses = []
sites = {
    'Узнать топовую песню в чартах': ['https://music.apple.com/ru/playlist/%D1%82%D0%BE%D0%BF-100-%D0%B2-%D0%BC%D0%B8%D1%80%D0%B5/pl.d25f5d1181894928af76c85c967f8f31',
                                      'songs-list-row__song-name svelte-1yo4jst',
                                      'В сегоднящних чартах песня: '],
    'Узнать, в какую популярную игру сыграть': [f'https://store.steampowered.com/search/?snr=1_5_9__12&term={choice(categories)}',
                                     'title',
                                     'Попробуй поиграть в '],
    'Узнать одно из новейших кино': ['https://www.kinoafisha.info/rating/movies/2022/',
                                      'movieItem_title',
                                      'На данный момент один из топовых фильмов: ']

}


def parse(url: str, parse_method: str, advanced_text=''):
    from bs4 import BeautifulSoup
    from requests import get
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find_all(class_=parse_method)
    if len(content) < 2:
        return advanced_text + content[0].text
    return advanced_text + choice(content).text


res = ''


@app.route('/', methods=['POST'])
def index():
    global responses, res
    if request.method == 'POST':
        chosen = request.data.decode('utf-8')
        responses.append(chosen)
        res = parse(sites[chosen][0], sites[chosen][1], advanced_text=sites[chosen][2])
        print(res)
        return jsonify({'res': res})

# Переосмысленный момент

# @app.route('/', methods=['GET'])
# def send():
#     if request.method == 'GET':
#         return jsonify({'res': res})


if __name__ == '__main__':
    app.run()
