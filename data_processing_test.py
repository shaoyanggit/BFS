# -*- coding: utf-8 -*-
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

text = "英雄集結：深度學習的魔法使們莉森揪 (alisonyang) iT邦新手 5 級 ‧ 點數  205 20999累計瀏覽數57人在追蹤站內簡訊 追蹤  個人背景 0發問 31文章 0回答 0邀請回答 0最佳解答 其他 鐵人檔案收藏的問題收藏的文章追蹤的問題追蹤的文章追蹤的tag追蹤的邦友Like的發問Like的回答Like的文章Like的留言問答討論問答回應文章留言文章回應聊天室訂閱列表 鐵人檔案  2019 iT 邦幫忙鐵人賽 回列表 AI & Data  英雄集結：深度學習的魔法使們 系列深度學習就像是個幻境之地，許多人曾經尋訪卻只得到碎片般的景色。在這裡，希望讓想成為深度學習的魔法使玩家能一覽深度學習之全貌，在30天後可以自信的說出：「沒錯，請你叫我『大魔法使』」。\r內容將包含深度學習的Learning map、最新研究技術與商業應用。  鐵人鍊成 ｜ 共 31 篇文章 ｜124 人訂閱 訂閱系列文 RSS系列文 4Like0留言6435瀏覽DAY 1  達標好文 [序幕] AI（人工智慧）、Machine Learning（機器學習）、 Deep Learning（深度學習）是什麼？  2018年堪稱是台灣的「AI 元年」，政府推動產業 AI 化，同時也不遺餘力的培養 AI 種子們。相信不管是在新聞媒體上或是公司內部都可常看到或聽到「AI」字眼... 2018-10-16 ‧ 由 莉森揪  分享 5Like1留言5226瀏覽DAY 2  達標好文 [地圖] 深度學習世界的魔法陣們  剛開始研究 deep learning 時，正好是 AlphaGo 跟南韓棋士李世乭對戰(2016年3月8日到3月15日)的前一兩個月，那時我們小組嘗試用 CN... 2018-10-17 ‧ 由 莉森揪  分享 4Like0留言4949瀏覽DAY 3  [魔法陣系列] Artificial Neural Network (ANN) 之術式解析  第一個魔法陣：Artificial Neural Network (ANN, 1943)首先先來看看 ANN 的結構：圖片來源：https://hack... 2018-10-18 ‧ 由 莉森揪  分享 4Like0留言4669瀏覽DAY 4  [魔法陣系列] Artificial Neural Network (ANN) 之術式啟動  上篇介紹 ANN 魔法陣結構：輸入層（Input Layer）、隱藏層（Hidden Layer）及輸出層（Output Layer）。此外，也解釋了神經元與激... 2018-10-19 ‧ 由 莉森揪  分享 4Like0留言3285瀏覽DAY 5  [實戰系列] 使用 TensorFlow 搭建一個 ANN 魔法陣（模型）  有了先前的 ANN 魔法陣教學後，該是來讓各位見習魔法使實戰演練了，前情提要請參見：[魔法陣系列] Artificial Neural Network (A... 2018-10-20 ‧ 由 莉森揪  分享 4Like1留言9476瀏覽DAY 6  [精進魔法] Regularization：減少 Overfitting ，提高模型泛化能力   當開始興致勃勃的嘗試畫魔法陣，搭建神經網絡模型時，也許會遇到下面的情形：哥布林之吶喊：我明明在訓練集表現很好啊，為什麼實際上線時結果卻崩潰了（抱頭）那你... 2018-10-21 ‧ 由 莉森揪  分享 3Like0留言3267瀏覽DAY 7  [精進魔法] Optimization：優化深度學習模型的技巧（上）  上篇提到怎麼避免 Overfitting 的技巧，本文要帶給大家的是如何優化深度學習，提高模型的效能。Batch & Mini batch深度學習每... 2018-10-22 ‧ 由 莉森揪  分享 5Like0留言5848瀏覽DAY 8  [精進魔法] Optimization：優化深度學習模型的技巧（中）－ Adaptive Learning Rates  前情提要在 [精進魔法] Optimization：優化深度學習模型的技巧（上）一文中提及了下面三種優化 deep learning 模型的作法：Batc... 2018-10-23 ‧ 由 莉森揪  分享 3Like0留言5019瀏覽DAY 9  [精進魔法] Optimization：優化深度學習模型的技巧（下）－ Batch Normalization  本文主題是「Batch Normalization」，Ian Goodfellow 大大在《Deep Learning》一書中是這麼描述 Batch Norma... 2018-10-24 ‧ 由 莉森揪  分享 3Like0留言1920瀏覽DAY 10  [魔王出沒] 深度學習中的魔王軍簡介  其實這篇應該先寫於《精進魔法》系列之前的，但沒關係，只要有 [地圖] 深度學習世界的魔法陣們 指引，你能夠照你想要挑戰的項目去學習。以下介紹深度學習的魔王們，... 2018-10-25 ‧ 由 莉森揪  分享 上一頁1234下一頁莉森揪的鐵人檔案莉森揪的收藏 收藏的問題收藏的文章莉森揪的追蹤 追蹤的問題追蹤的文章追蹤的tag追蹤的邦友莉森揪的Like Like的發問Like的回答Like的文章Like的留言莉森揪的紀錄 問答討論問答回應文章留言文章回應聊天室莉森揪的訂閱列表電週文化事業版權所有、轉載必究 | Copyright © iThome刊登廣告授權服務服務信箱隱私權聲明與會員使用條款iT邦幫忙使用說明At輸入對方的帳號或暱稱 Loading  找不到結果。 標記{{ result.label }}{{ result.account }}關閉"

chi_text = "".join(re.compile(r'[\u4e00-\u9fa5]').findall(text))
if len(chi_text) > 0:
    chi_text = ws([chi_text])
    chi_text = list(filter(lambda a: a not in chi_stopWords, chi_text))

# 備用，感覺效果沒有比較好
# eng_text = " ".join(re.compile(r'[\u0061-\u007a]+').findall(text.lower()))
# if len(eng_text) > 0:
#     eng_text = gensim.parsing.preprocess_string(eng_text)

eng_text = " ".join(re.compile(r'[\u0061-\u007a]+').findall(text.lower()))
if len(eng_text) > 0:
    eng_text = gensim.parsing.remove_stopwords(eng_text)
    eng_text = gensim.utils.tokenize(eng_text)

tokens = chi_text + eng_text
dictionary = gensim.corpora.Dictionary([tokens])
print(dictionary)