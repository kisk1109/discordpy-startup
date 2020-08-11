from discord.ext import commands
from asyncio import sleep
import os
import traceback
import discord
import re 

bot = commands.Bot(command_prefix='?')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()
    

@bot.command()
async def gomi(ctx):
    if not discord.opus.is_loaded(): 
        discord.opus.load_opus("heroku-buildpack-libopus")
    voice_client = ctx.message.guild.voice_client
    vc = ctx.author.voice.channel
    await ctx.author.voice.channel.connect()
    source = discord.FFmpegPCMAudio("gomikasu.wav")
    ctx.message.guild.voice_client.play(source)
            
@bot.command()
async def 全部消えちゃえ(cmd):
        if cmd.author.guild_permissions.administrator:
            await cmd.channel.purge()
            await cmd.channel.send('テキストチャンネルを灰にしてしまいました')
        else:
            await cmd.channel.send('何様のつもり？')
            
@client.event 
async def on_ready():
    CHANNEL_ID = '658980967876263936' 
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('BOT起動')
    
bot.run(token)
