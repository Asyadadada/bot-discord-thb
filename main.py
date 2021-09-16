import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.command()
async def hello(ctx):
    await ctx.reply('Helo Asu!')

Token = #Token ada di channel dev bot

bot.run(Token)
