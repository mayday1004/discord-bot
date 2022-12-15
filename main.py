import datetime, asyncio, os
import nextcord
from nextcord.ext import commands
from tweepy_setup import check_tweets
from dotenv import load_dotenv
load_dotenv()
intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

current_active_channel = []

#設置頻道要獲取的推文:$初始化 <頻道ID> <欲搜尋的關鍵字> <獲取讚數以上推文>
@bot.command(name="初始化")
async def SendMessage(ctx, room_id, keyword, faves):
    await ctx.send(f"頻道ID: {room_id} 無誤，開始獲取推文")
    await auto_message(str(ctx.command), int(room_id), keyword, int(faves))

#設置頻道停止獲取推文:$停止推文 <頻道ID>
@bot.command(name="停止推文")
async def SendMessage(ctx, room_id):
    await auto_message(str(ctx.command), int(room_id), " ", 50)

#執行發送推文
async def auto_message(command, room_id, keyword, faves=50):
    if command == "停止推文":
        current_active_channel.remove(room_id)
        channel = bot.get_channel(room_id)
        await channel.send(f"頻道ID: {room_id} 已暫停獲取推文")
    else:
        current_active_channel.append(room_id)

    while room_id in current_active_channel:
        get_tweets = check_tweets(keyword, faves)
        channel = bot.get_channel(room_id)
        if len(get_tweets) > 0:
            for tweet in get_tweets:
                await channel.send(tweet)
        #設置推文發送間隔
        now = datetime.datetime.now()
        then = now+datetime.timedelta(hours = 2)
        wait_time = (then-now).total_seconds()
        await asyncio.sleep(wait_time)

@bot.event
async def on_ready():
    print(f"Loggined in as: {bot.user.name}")
    #機器人狀態
    game = nextcord.Game("馬應龍的推特")
    await bot.change_presence(status=nextcord.Status.online, activity=game)

if __name__ == '__main__':
    bot.run(os.getenv("BOT_TOKEN"))