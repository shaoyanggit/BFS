from flask import Flask, request
from flask_cors import CORS
from flask_api import status
import csv
import json
from full_text_crawler import craw_data
from search_engine_core import build_dictionary, BookmarkFullTextCorpus, build_model, search
import gensim

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    with open("bookmarks.csv", "w", encoding='utf-8') as outfile:
        fieldnames = ['title', 'url']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        json_str = str(request.data, encoding='utf-8')
        data = json.loads(json_str)
        writer.writerows(data)

    craw_data("bookmarks.csv", "full_text.csv")
    
    build_dictionary('full_text.csv')
    corpus = BookmarkFullTextCorpus(gensim.utils.SaveLoad.load('bookmarks_token.dict'), 'full_text.csv')
    build_model(corpus, 'full_text.csv')

    content = {'message': 'build index done'}
    return content, status.HTTP_200_OK

@app.route('/search')
def query():
    lsi_model = gensim.models.lsimodel.LsiModel.load('bookmark_lsi_model.lsi')
    lsi_index = gensim.similarities.Similarity.load('bookmark_lsi_index.index')
    corpus = BookmarkFullTextCorpus(gensim.utils.SaveLoad.load('bookmarks_token.dict'), 'full_text.csv')
    results = search(request.args.get('query'), corpus, lsi_model, lsi_index)
    return '\n'.join(results)

if __name__ == '__main__':
    app.run(port=2020)