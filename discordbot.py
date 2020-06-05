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
async def ウルフ(ctx):
    await ctx.send('<@418022256057516033>')
    await ctx.send('<@418022256057516033>')
    await ctx.send('<@418022256057516033>')
    await ctx.send('<@418022256057516033>')
    
@bot.command()
async def daipan(ctx):
    await ctx.send('ヤバイわよ！',file=discord.File('tenor.gif'))
    

@bot.command()
async def 三宅(ctx):
    await ctx.send('てすと',file=discord.File('miyake.png'))
    

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
            
# BOT動作プログラム
@client.event
async def on_message(message):
    # 送り主がBotだった場合反応したくないので
    if client.user != message.author:
        # 削除コマンド
        if message.content.startswith("!delchat "):
            #役職比較
            if cmd.author.guild_permissions.administrator:
                msgch = client.get_channel(658980967876263936)
                # メッセージを格納
                delcmd = message.content
                # 入力メッセージのリスト化
                delcmd_ = delcmd.split()
                # 入力メッセージのint化
                delcmd_int = int(delcmd_[1])
                # 入力メッセージの単語数
                delcmd_c = len(delcmd_)
                if delcmd_c == 2 and delcmd_int <= 50 and delcmd_int > 1:
                    # メッセージ取得
                    msgs = [msg async for msg in client.logs_from(message.channel, limit=(delcmd_int+1))]
                    await client.delete_messages(msgs)
                    delmsg = await msgch.send('削除が完了しました')
                    await sleep(5)
                    await client.delete_message(delmsg)
                else:
                    # エラーメッセージを送ります
                    delmsg = await msgch.send( "コマンドが間違っています。[!delchat *] *:2～50")
                    await sleep(5)
                    await client.delete_message(delmsg)
                    
            else:
                # エラーメッセージを送ります
                delmsg = await msgch.send("admin権限がありません。")
                await sleep(5)



@client.event 
async def on_ready():
    CHANNEL_ID = '658980967876263936' 
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('BOT起動')
    
bot.run(token)
