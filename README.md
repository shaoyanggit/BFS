# BFS (Bookmark Full-Text Search)
encoding: CRLF/UTF-8

## Installation

### Download ckip model
```
# -*- coding: utf-8 -*-
from ckiptagger import data_utils
data_utils.download_data_gdown("./")
```

### Install python packages
```
pip install -r requirements.txt
```

### Load extension for Chrome
* Settings->Extensions->turn on Developer mode
* Load unpacked->select file "manifest.json"->done

## Run Server
```
cd server
python bfs.py
```

## References
* Building Search Engines with Gensim: https://christop.club/talks/tripython_2015/#/
* Debounce: https://github.com/lishengzxc/bblog/issues/7
* [mozilla-JavaScript-APIs](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API)
