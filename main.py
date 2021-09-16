import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.command()
async def hello(ctx):
    await ctx.reply('Helo Gaes')

@bot.command()
async def test(ctx):
    await ctx.reply('Test tost')

token = 'ODg4MDUxMjc2NDM5NTAyOTA4.YUNEMw.dy9Dq2BoeRRxILMrxWkQsOqNNVo'

bot.run(token)
