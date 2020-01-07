# BFS
encoding: CRLF/UTF-8

## requirements

### Download ckip model
```
# -*- coding: utf-8 -*-
from ckiptagger import data_utils
data_utils.download_data_gdown("./")
```

### install python packages
```
pip install -r requirements.txt
```

## run server
```
cd server
python bfs.py
```

## load extension for Chrome
* Settings->Extensions->turn on Developer mode
* Load unpacked->select file "manifest.json"->done

## references
* Building Search Engines with Gensim: https://christop.club/talks/tripython_2015/#/
* Debounce: https://github.com/lishengzxc/bblog/issues/7
- [mozilla-JavaScript-APIs](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API)
