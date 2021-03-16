from flask import Flask
from tasks import *
import celery

app = Flask(__name__)


@app.route('/wiki/start')
def start():
    print('qwe')
    get_wiki_data.apply_async()
    return 'Start parsing, go to /wiki/result'


@app.route('/wiki/result')
def result():
    try:
        with open('data.json') as json_file:
            data = json.load(json_file)
    except:
        return 'not ready yet'


if __name__ == '__main__':
    app.run(debug=True)
