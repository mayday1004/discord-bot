import datetime, asyncio, os
import nextcord
from nextcord.ext import commands
from tweepy_setup import search_result
from dotenv import load_dotenv
load_dotenv()

auto_message_switch = False

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

#設置頻道要獲取的推文:$初始化 <頻道ID> <欲搜尋的關鍵字>
@bot.command(name="初始化")
async def SendMessage(ctx, room_id, keyword):
    await ctx.send(f"頻道ID: {room_id} 無誤，開始獲取推文")
    await auto_message(int(room_id), keyword)


async def auto_message(room_id, keyword):
    while True:
        get_tweets = search_result(keyword)
        channel = bot.get_channel(room_id)
        if len(get_tweets) > 0:
            for tweet in get_tweets:
                await channel.send(tweet)
        now = datetime.datetime.now()
        then = now+datetime.timedelta(hours = 1)
        wait_time = (then-now).total_seconds()
        await asyncio.sleep(wait_time)

@bot.event
async def on_ready():
    print(f"Loggined in as: {bot.user.name}")
    game = nextcord.Game("馬應龍的推特")
    await bot.change_presence(status=nextcord.Status.online, activity=game)

if __name__ == '__main__':
    bot.run(os.getenv("BOT_TOKEN"))