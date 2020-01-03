from discord.ext import commands
import os
import traceback
import discord

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
async def test(ctx):
    await ctx.send('!join')
    await ctx.send('!play https://www.youtube.com/watch?v=s582L3gujnw')
    
@bot.command()
async def what(ctx)
     await ctx.send('ヤバイわよ！', { file: { attachment: tenor.gif } })
    
@client.event
async def on_ready():
    CHANNEL_ID = 658980967876263936# 任意のチャンネルID(int)
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('BOT起動')
    
bot.run(token)
