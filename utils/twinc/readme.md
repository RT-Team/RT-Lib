![](https://cdn.discordapp.com/attachments/720200569603751976/810504822075555910/Screenshot_20210214-223527.jpg)
# Twinc
Twitterの取得ライブラリです。

# 必要なモジュール
* aiohttp
* requests
* bs4

# How to use - 個人
pythonでそのまま実行すると`username>`とでます。
その時に見たいツイートを投稿している人のユーザーIDを入力します。
  (*@tasuren1*だったらtasuren1を入力)

# How to use - モジュール
非非同期で取得する場合はget_tweets()で取得できます。
非同期の場合はasync_get_tweets()で取得できます。
どちらともジェネレーターで引数に目的の人物名を入れます。
 (人物名は@tasuren1の場合tasuren1を入れてください。)
リストとして取る場合は`list()`を使ってください。
## import
このファイルをImportしてから使います。
```python
import twinc
```
## 非非同期でのtasuren1を取得する例
```python
for data in twinc.get_tweets('tasuren1'):
    print(data)
```
## 非同期でのtasuren1を取得する例
```python
for data in (await twinc.async_get_tweets('tasuren1')):
    print(data)        
```
## 戻り値
以下のような辞書型です。
```json
{
  "author": {
    "avatar": "https://pbs.twimg.com/profile_images/1356961072964493319/yHowjeIs_bigger.jpg",
    "name": "tasuren",
    "screenName": "@tasuren1",
    "url": "https://twitter.com/tasuren1"
  },
  "tweet": {
    "id": "1358735837182087168",
    "retweet": False,
    "text": "#こんな壁紙でも引かないよって人RT\n"
            "ハッハッハ\n"
             "電柱の壁紙とは趣があるだろう！\n"
            "\n"
            "え?もう片方?なんだろうね\n"
            "  ",
     "time": "2021-02-08T11:14:02+0000",
     "url": "https://twitter.com/tasuren1/status/1358735837182087168"
  }
}
```
# ライセンス
MIT LICENSE
