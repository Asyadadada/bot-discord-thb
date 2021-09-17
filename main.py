import discord
from discord.ext import commands
import kbbi as Kamus

bot = commands.Bot(command_prefix='gxt!')

def get_definisi(kata):
  try:
    return f"```\n{Kamus.KBBI(kata).__str__(contoh=False)}```"
  except kbbi.kbbi.TidakDitemukan:
    return "```Maaf, entri tidak ditemukan.```"

@bot.command()
async def kbbi(ctx, arg):
    await ctx.reply(get_definisi(arg))

@bot.command()
async def hello(ctx):
    await ctx.reply('Helo Gaes')

@bot.command()
async def test(ctx):
    await ctx.reply('Test tost')

token = '#adadidc

bot.run(token)
