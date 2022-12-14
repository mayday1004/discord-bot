import os
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


result_lists = set()
def search_result(keyword):
    clone_result_lists = result_lists.copy()
    #使用 tweepy 進行推特搜索
    search_word = f"{keyword} min_faves:50 filter:links -filter:replies"
    for tweets in api.search_tweets(q=search_word, result_type="recent", count=100):
        human_time = str(tweets.created_at).split("+")[0]
        tweet_result_format = f"{human_time}  |  https://twitter.com/user/status/{tweets.id}"
        
        if len(clone_result_lists) == 0:
            #第一次搜尋
            result_lists.add(tweet_result_format)
        else:
            #第二次以上搜尋，判斷set有沒有已經送出的推文? 有>移除，沒有>新增
            if tweet_result_format in result_lists:
                result_lists.remove(tweet_result_format)
            else:
                result_lists.add(tweet_result_format)

    return result_lists
            