import json
import requests
import re
from bs4 import BeautifulSoup

with open("bookmarks_2019_11_6.html", encoding='utf-8') as f:
    soup = BeautifulSoup(f, "lxml")

a_tags = soup.find_all('a')

data = []
error = 0

for i, a_tag in enumerate(a_tags):
    print(i)
    # handle plain text
    try:
        r = requests.get(a_tag.get('href'))
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text, 'lxml')
            if soup.body != None:
                for s in soup(["script", "style", "nav", "button"]):
                    s.extract()
                plain_text = soup.body.get_text()
                plain_text = re.sub(r' {2,}', " ", plain_text)
                plain_text = re.sub(r'\t', "", plain_text)
                plain_text = plain_text.replace("\n", "")

        # handle categories
        dls = [p for p in a_tag.findParents('dl')][:-1]
        cats = [dl.findPrevious().contents[0].string for dl in dls]
        if "書籤列" in cats:
            cats.remove("書籤列")
        cats.reverse()
        data.append({'id': i, 'title': a_tag.string, 'url': a_tag.get('href'), 'categories': cats, 'plain_text': plain_text})
    except:
        error += 1
    
    if i >= 10:
        break

with open("data_sample.json", "w", encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False)
    outfile.close()

print("done with {} errors in {} data".format(error, len(a_tags)))