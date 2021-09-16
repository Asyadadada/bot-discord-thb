import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.command()
async def hello(ctx):
    await ctx.reply('Helo Gaes')

@bot.command()
async def test(ctx):
    await ctx.reply('Test tost')

token = '#adadidc

bot.run(token)
