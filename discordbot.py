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
async def p(ctx,age1,age2):
    voice_client = ctx.message.guild.voice_client
    vc = ctx.author.voice.channel
    music = 
    if not discord.opus.is_loaded(): 
        discord.opus.load_opus("heroku-buildpack-libopus")
    if message.author.voice_channel is None:
        await ctx.send('ボイスチャンネルに参加した上で、もう一度実行してください。')
        return
    if voice == None:
        voice = await client.join_voice_channel(message.author.voice_channel)
    # 接続しているかを確認
    elif(voice.is_connected() == True):
    #voicechannelに接続
        await ctx.author.voice.channel.connect()
    source = discord.FFmpegPCMAudio("gomikasu.wav")
    ctx.message.guild.voice_client.play(source)

@client.event
async def on_ready():
    CHANNEL_ID = '658980967876263936' # 任意のチャンネルID(int)
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('BOT起動')
    
bot.run(token)
