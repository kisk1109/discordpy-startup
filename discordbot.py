from discord.ext import commands
import os
import traceback
import discord
import re 

bot = commands.Bot(command_prefix='?')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@bot.event #エラーメッセージ
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def ウルフ(ctx):
    await ctx.send('<@418022256057516033>')
    await ctx.send('<@418022256057516033>')
    await ctx.send('<@418022256057516033>')
    await ctx.send('<@418022256057516033>')
    
@bot.command()
async def daipan(ctx):
    await ctx.send('ヤバイわよ！',file=discord.File('tenor.gif'))
    
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
async def cleanup(cmd):
        if cmd.author.guild_permissions.administrator:
            await cmd.channel.purge()
            await cmd.channel.send('塵一つ残らないね！')
        else:
            await cmd.channel.send('何様のつもり？')
            
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
