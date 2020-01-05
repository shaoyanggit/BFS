from flask import Flask, request
from flask_cors import CORS
from flask_api import status
import csv
import json
from full_text_crawler import craw_data
from search_engine_core import build_dictionary, BookmarkFullTextCorpus, build_model, search, rebuild_dictionary
import gensim
import datetime

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    start_time = datetime.datetime.now()
    with open("bookmarks.csv", "w", encoding='utf-8') as outfile:
        fieldnames = ['title', 'url']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        json_str = str(request.data, encoding='utf-8')
        data = json.loads(json_str)
        writer.writerows(data)

    craw_data(target_file="bookmarks.csv", out_file="full_text.csv")
    
    build_dictionary('full_text.csv')
    corpus = BookmarkFullTextCorpus(gensim.utils.SaveLoad.load('bookmarks_token.dict'), 'full_text.csv')
    build_model(corpus, 'full_text.csv')

    end_time = datetime.datetime.now()
    print('start at {}, end at {}'.format(start_time, end_time))
    content = {'message': 'build index done'}
    return content, status.HTTP_200_OK

@app.route('/search')
def query():
    lsi_model = gensim.models.lsimodel.LsiModel.load('bookmark_lsi_model.lsi')
    lsi_index = gensim.similarities.Similarity.load('bookmark_lsi_index.index')
    corpus = BookmarkFullTextCorpus(gensim.utils.SaveLoad.load('bookmarks_token.dict'), 'full_text.csv')
    results = search(request.args.get('query'), corpus, lsi_model, lsi_index)
    
    response = app.response_class(
        response=json.dumps(results),
        status=200,
        mimetype='application/json'
    )
    # return '\n'.join(results)
    return response

@app.route('/new', methods=['GET', 'POST'])
def new_bookmark():
    start_time = datetime.datetime.now()
    with open("bookmarks.csv", "a", encoding='utf-8') as outfile:
        fieldnames = ['title', 'url']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        json_str = str(request.data, encoding='utf-8')
        data = json.loads(json_str)
        writer.writerow(data)

        craw_data(target=data, out_file="full_text.csv")

    rebuild_dictionary('full_text.csv')
    corpus = BookmarkFullTextCorpus(gensim.utils.SaveLoad.load('bookmarks_token.dict'), 'full_text.csv')
    
    # model全部重建，這裡不能使用add_documents，因為字典也重建了
    # 參考https://github.com/RaRe-Technologies/gensim/issues/1178
    build_model(corpus, 'full_text.csv') 

    end_time = datetime.datetime.now()
    print('start at {}, end at {}'.format(start_time, end_time))

    content = {'message': 'rebuild index done'}
    return content, status.HTTP_200_OK

if __name__ == '__main__':
    app.run(port=2020)