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

class BookmarkFullTextCorpus():
    def __init__(self, archive_path):
        self.path = archive_path
        self.dictionary = gensim.corpora.Dictionary(self.iter_texts())
        
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
        pass  # let's not look at this :-)

content = BookmarkFullTextCorpus('data_sample.csv')

index = gensim.similarities.Similarity('data_sample.csv',
                                       content, 
                                       num_features=len(content.dictionary),
                                       num_best=15)
query_bow = content.dictionary.doc2bow(preprocess('tensorflow'))
print(query_bow)
print(index[query_bow])