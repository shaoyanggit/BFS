# -*- coding: utf-8 -*-
import csv
from ckiptagger import WS
from opencc import OpenCC
import re
import gensim

cc = OpenCC('s2tw')
ws = WS("./data")

chi_stopWords=[]
with open('stopWords.txt', 'r', encoding='UTF-8') as file:
    for data in file.readlines():
        data = data.strip()
        chi_stopWords.append(data)

def preprocess(text):
    chi_tokens = []
    chi_text = "".join(re.compile(r'[\u4e00-\u9fa5]').findall(text))
    if len(chi_text) > 0:
        chi_text_seg = ws([chi_text])[0]
        chi_tokens = list(filter(lambda a: a not in chi_stopWords, chi_text_seg))

    eng_tokens = []
    eng_text = " ".join(re.compile(r'[\u0061-\u007a]+').findall(text.lower()))
    if len(eng_text) > 0:
        eng_text = gensim.parsing.remove_stopwords(eng_text)
        eng_tokens = list(gensim.utils.tokenize(eng_text))

    tokens = chi_tokens + eng_tokens
    return tokens

def build_dictionary(csv_file):
    def iter_texts():
        with open(csv_file, encoding='utf-8') as f:
            for row in csv.DictReader(f):
                yield preprocess(row["plain_text"])
    
    dictionary = gensim.corpora.Dictionary(iter_texts())
    dictionary.save('bookmarks_token.dict')
    print('build dictionary done')

class BookmarkFullTextCorpus():
    def __init__(self, dictionary, csv_file):
        self.dictionary = dictionary
        self.path = csv_file
    
    def iter_texts(self):
        with open(self.path, encoding='utf-8') as f:
            for row in csv.DictReader(f):
                yield preprocess(row["plain_text"])

    def __iter__(self):
        for document in self.iter_texts():
            yield self.dictionary.doc2bow(document)

    def __len__(self):
        return self.dictionary.num_docs
    
    def get_original(self, key):
        with open(self.path, encoding='utf-8') as f:
            for i, row in enumerate(csv.DictReader(f)):
                if i == key:
                    return row

def build_model(corpus, csv_file):
    lsi = gensim.models.LsiModel(corpus,
                                num_topics=100,
                                power_iters=10,
                                id2word=corpus.dictionary)

    lsi_index = gensim.similarities.Similarity(csv_file,
                                            lsi[corpus],
                                            num_features=lsi.num_topics,
                                            num_best=15)

    lsi.save('bookmark_lsi_model.lsi')
    lsi_index.save('bookmark_lsi_index.index')
    print('build model done')

def search(query, corpus, model, index):
    query_bow = corpus.dictionary.doc2bow(preprocess(query))
    
    results = []
    for doc, percent in index[model[query_bow]]:
        original_doc = corpus.get_original(doc)
        results.append("{:.5f} => {} ({})".format(percent, original_doc['title'], original_doc['url']))

    return results

if __name__ == '__main__':
    build_dictionary('full_text.csv')

    corpus = BookmarkFullTextCorpus(gensim.utils.SaveLoad.load('bookmarks_token.dict'), 'full_text.csv')

    build_model(corpus, 'full_text.csv')

    lsi_model = gensim.models.lsimodel.LsiModel.load('bookmark_lsi_model.lsi')
    lsi_index = gensim.similarities.Similarity.load('bookmark_lsi_index.index')

    print('\n'.join(search('遊戲', corpus, lsi_model, lsi_index)))