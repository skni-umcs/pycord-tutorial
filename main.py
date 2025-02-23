# For extracting TOKEN from the environment
from dotenv import load_dotenv
import os

# For pseudorandom number generation
import random

# The main library for using discord API
import discord


load_dotenv() # Load all the variables from the env file
bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")


bot.run(os.getenv('TOKEN')) # Runs the bot with the token

# Repo: https://github.com/skni-umcs/pycord-tutorial