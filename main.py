import datetime
import asyncio
import os
import nextcord
from nextcord.ext import commands
from tweepy_setup import check_tweets, stop_tweets
from dotenv import load_dotenv

load_dotenv()
intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

current_active_channel = set()

# 確認機器人有在運行
@bot.command(name="log")
async def SendMessage(ctx):
    await ctx.send(f"活動中頻道列表 : {current_active_channel}")
    if ctx.channel.id in current_active_channel:
        await ctx.send("當前頻道正接收推文")
    else:
        await ctx.send("當前頻道沒有接收任何推文")


# 設置頻道要獲取的推文:$推特搜尋 <欲搜尋的關鍵字> <獲取讚數以上推文>
@bot.command(name="推特搜尋")
async def SendMessage(ctx, keyword, exclude_words, faves):
    keyword = keyword.replace("!", "#")
    exclude_words = exclude_words.split(",")
    current_active_channel.add(int(ctx.channel.id))
    await ctx.send(f"頻道ID: {ctx.channel.id} 開始獲取推文")
    await auto_message(int(ctx.channel.id), keyword, exclude_words, int(faves))


# 設置頻道停止獲取推文:$停止推文
@bot.command(name="停止推文")
async def SendMessage(ctx):
    current_active_channel.remove(int(ctx.channel.id))
    stop_tweets(int(ctx.channel.id))
    await ctx.send(f"頻道ID: {ctx.channel.id} 已暫停獲取推文")


# 刪除頻道消息，至多100則:
@commands.has_permissions(manage_messages=True)
@bot.command(name="清理對話")
async def SendMessage(ctx, num=100):
    await ctx.channel.purge(limit=num)


# 執行發送推文
async def auto_message(room_id, keyword, exclude_words, faves):
    while room_id in current_active_channel:
        get_tweets = check_tweets(room_id, keyword, exclude_words, faves)
        channel = bot.get_channel(room_id)
        if len(get_tweets) > 0:
            for tweet in get_tweets:
                await channel.send(tweet)
        # 設置推文發送間隔
        now = datetime.datetime.now()
        then = now + datetime.timedelta(hours=1)
        wait_time = (then - now).total_seconds()
        await asyncio.sleep(wait_time)


@bot.event
async def on_ready():
    print(f"Loggined in as: {bot.user.name}")
    # 機器人狀態
    act = nextcord.Activity(
        type=nextcord.ActivityType.listening, name="片恋艶花 - 藤乃靜留"
    )  # 正在聽
    # game = nextcord.Game("馬應龍的推特") #正在玩
    # watch = nextcord.Activity(type=nextcord.ActivityType.watching, name="影片名稱") #正在看
    # stream = nextcord.Streaming(name="直播間", url=jdata["twitch_url"]) #正在直播
    await bot.change_presence(status=nextcord.Status.online, activity=act)


if __name__ == "__main__":
    bot.run(os.getenv("BOT_TOKEN"))
