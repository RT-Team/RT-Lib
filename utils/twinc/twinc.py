# Twinc by tasuren
from requests import get
from aiohttp import ClientSession
from bs4 import BeautifulSoup as bs

from json import decoder



def NoneTweet():
    yield None

# スクレイピングする
def twitter2soup(html):
    soup = bs(html.replace("<br>","\n"),"html.parser")
    tweets = soup.find_all("li",class_="timeline-TweetList-tweet customisable-border")

    for t in tweets:
        metadata = t.find("div",class_="timeline-Tweet-metadata")
        yield {
            "author": {
                "name"      : t.find("span",class_="TweetAuthor-name Identity-name customisable-highlight").get("title"),
                "screenName": t.find("span",class_="TweetAuthor-screenName Identity-screenName").get("title"),
                "avatar"    : t.find("img",class_="Avatar").get("data-src-2x"),
                "url"       : t.find("a",class_="TweetAuthor-link Identity u-linkBlend").get("href")
            },
            "tweet" : {
                "text"   : t.find("p",class_="timeline-Tweet-text").text,
                "time"   : t.find("time",class_="dt-updated").get("datetime"),
                "id"     : t.find("div").get("data-rendered-tweet-id"),
                "retweet": True if t.find("div","timeline-Tweet-retweetCredit") else False,
                "url"    : metadata.find("a").get("href"),
            }
        }

# 取得
def get_tweets(username):
    r = get(f"https://syndication.twitter.com/timeline/profile?screen_name={username}")
    try:data = r.json()["body"]
    except decoder.JSONDecodeError:return NoneTweet()
    return twitter2soup(data)

# 非同期版取得
async def async_get_tweets(username):
    async with ClientSession() as session:
        async with session.get(f"https://syndication.twitter.com/timeline/profile?screen_name={username}") as r:
            try:data = (await r.json())["body"]
            except decoder.JSONDecodeError:return NoneTweet()
    return twitter2soup(data)



if __name__ == "__main__":
    for data in get_tweets(input("USERNAME>")):
        if data:
            author,tweet = data["author"],data["tweet"]

            print(f'''-=- Tweet Retweet:{tweet["retweet"]} -=-
* author :
{author["name"]} / {author["screenName"]}
  ({author["url"]})
* time :
{tweet["time"]}
* text :
{tweet["text"]}
* url : 
{tweet["url"]}
* id :
{tweet["id"]}
''')
        else:
            print("Tweetが見つかりませんでした。")
