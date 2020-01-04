from discord.ext import commands
import os
import traceback
import discord
import re 

bot = commands.Bot(command_prefix='?')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def まじ反応しろ(ctx):
    await ctx.send('<@418022256057516033>')
    await ctx.send('<@418022256057516033>')
    await ctx.send('<@418022256057516033>')
    await ctx.send('<@418022256057516033>')
    
@bot.command()
async def daipan(ctx):
    await ctx.send('ヤバイわよ！',file=discord.File('tenor.gif'))
    
@bot.command()
async def gomi(ctx):
    voice = await client.join_voice_channel(message.author.voice_channel)
    player = voice.create_ffmpeg_player('gomikasu.wav')
    player.start()
    

# 存在しないコマンドが打たれた場合の処理
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(f"{ctx.author.name}さん、*{ctx.message.content}*というコマンドはありませんよ！")
    raise error
    
@bot.event
async def on_massage(msg):
    if message.author.bot:
        return
    if re.search(r'ゴミカス',msg,content):
    voice = await client.join_voice_channel(message.author.voice_channel)
    player = voice.create_ffmpeg_player('gomikasu.wav')
    player.start()
    
# ping-通信速度を測る
@bot.command()
async def ping(ctx):
    before = time.monotonic()
    embed = discord.Embed(description="Pong!")
    msg = await ctx.send(embed=embed)
    ping = (time.monotonic() - before) * 1000
       
    pingmsg = "反応速度:\n{0}ms".format(int(ping))
    embed = discord.Embed(description=pingmsg)
    await msg.edit(embed=embed)


@client.event
async def on_ready():
    CHANNEL_ID = 658980967876263936# 任意のチャンネルID(int)
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('BOT起動')
    
bot.run(token)
