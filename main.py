#For token importing
from dotenv import load_dotenv
import os

#The main library for using discord API
import discord

#Ai integration file located in the same folder as main.py
from ai import ask_ai

load_dotenv() # load all the variables from the env file
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

@bot.slash_command(name = "ai", description = "Use AI")
async def ai(ctx: discord.ApplicationContext, prompt: str):
    await ctx.response.defer() #important line so that interaction doesn't timeout before AI answers
    await ctx.respond(ask_ai(prompt))

bot.run(os.getenv('TOKEN')) #Runs the bot with the token

#Repo: https://github.com/skni-umcs/pycord-tutorial