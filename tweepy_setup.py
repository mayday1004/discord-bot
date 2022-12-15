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


keyword_dict = {}

def search_tweets(keyword, faves):
    search_results = []
    #使用 tweepy 進行推特搜索
    search_word = f"{keyword} min_faves:{faves} filter:media -filter:replies -filter:retweets"
    for tweets in api.search_tweets(q=search_word, result_type="recent", count=100):
        human_time = str(tweets.created_at).split("+")[0]
        tweet_result_format = f"{human_time}  |  https://twitter.com/user/status/{tweets.id}"
        search_results.insert(0, tweet_result_format)
    return search_results

def check_tweets(keyword, faves):
    search_results = search_tweets(keyword, faves)
    if keyword not in keyword_dict:
        #第一次搜尋
        keyword_dict[keyword] = search_results
        return search_results
    else:
        #第二次或以上搜尋，篩選掉已經發過的內容
        filtered_search_results = search_results.copy()
        for tweet in keyword_dict[keyword]:
            filtered_search_results.remove(tweet)
            
        keyword_dict[keyword] = search_results
        return filtered_search_results