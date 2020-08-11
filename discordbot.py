from discord.ext import commands
from asyncio import sleep
import os
import traceback
import discord
import re 

bot = commands.Bot(command_prefix='?')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

if not discord.opus.is_loaded():
    discord.opus.load_opus("heroku-buildpack-libopus")
    

@bot.command()
async def gomi(ctx):
        """指定された音声ファイルを流します。"""
    voice_client = ctx.message.guild.voice_client

    if not voice_client:
        await ctx.send("Botはこのサーバーのボイスチャンネルに参加していません。")
        return
    ffmpeg_audio_source = discord.FFmpegPCMAudio("gomikasu.wav")
    voice_client.play(ffmpeg_audio_source)
            
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
