# BFS

encoding: CRLF/UTF-8

## References
- [mozilla-JavaScript-APIs](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API)

## Problems

- bfs.js裡，line1的語句無法執行，原因尚不清楚。
bookmarks的執行權限已經有了，宣告在manifest.json的permissions處。
相關參考：[API-bookmarks-getTree](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/bookmarks/getTree)
(12-15 Y) 改用background scripts。(1-1 Y)

- 瀏覽器的接口已經清楚了，暫時只考慮Chrome。

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

## references
* Building Search Engines with Gensim: https://christop.club/talks/tripython_2015/#/