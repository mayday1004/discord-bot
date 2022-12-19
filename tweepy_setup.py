import os, ast
from datetime import date
import tweepy
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_KEY_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# 設置 tweepy API 密鑰和權限
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# 創建 tweepy API 實例
api = tweepy.API(auth)

keyword_dict = {}
with open("last_search_result.txt", "r") as last_search_result:
    string_search_result = last_search_result.read()
    if string_search_result:
        keyword_dict = ast.literal_eval(string_search_result)


def search_tweets(keyword, exclude_words, faves):

    # 使用 tweepy 進行推特搜索
    today = date.today()
    before_3_day = today.replace(day=today.day - 2)
    search_word = f"{keyword} min_faves:{faves} filter:media since:{before_3_day} -filter:replies -filter:retweets"
    search_results = api.search_tweets(q=search_word, result_type="recent", count=100)
    filtered_results = []

    # 排除指定關鍵字內容，如果有輸入排除關鍵字才執行
    if exclude_words[0]:
        for tweets in search_results.copy():
            for exclude in exclude_words:
                if exclude in tweets.text:
                    search_results.remove(tweets)
                    break

    for tweets in search_results:
        human_time = str(tweets.created_at).split("+")[0]
        tweet_result_format = (
            f"{human_time}  |  https://twitter.com/user/status/{tweets.id}"
        )
        filtered_results.insert(0, tweet_result_format)

    return filtered_results


def check_tweets(room_id, keyword, exclude_words, faves):
    room_id = str(room_id)
    search_results = search_tweets(keyword, exclude_words, faves)

    if room_id not in keyword_dict:
        # 第一次搜尋
        keyword_dict[room_id] = search_results
        with open("last_search_result.txt", "w") as last_search_result:
            last_search_result.write(str(keyword_dict))

        return search_results
    else:
        # 第二次或以上搜尋
        new_search_results = search_results.copy()
        for tweet in keyword_dict[room_id]:
            # 舊推文存在在新推文的話要移除
            if tweet in new_search_results:
                new_search_results.remove(tweet)

        keyword_dict[room_id] = search_results
        with open("last_search_result.txt", "w") as last_search_result:
            last_search_result.write(str(keyword_dict))

        return new_search_results


# 將搜尋關鍵字資料移除
def stop_tweets(room_id):
    room_id = str(room_id)
    keyword_dict.pop(room_id)
