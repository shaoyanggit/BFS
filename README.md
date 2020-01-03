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

## Download ckip model
```
# -*- coding: utf-8 -*-
from ckiptagger import data_utils
data_utils.download_data_gdown("./")
```

## TODO
* Stop word
    * 中文
    * 英文