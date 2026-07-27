import discord
from dotenv import load_dotenv
import os
import random

# load environment variables
load_dotenv()
bot = discord.Bot()

coinflips = bot.create_group("coins", "flip coins")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

coins = ["Heads", "Tails"]

@coinflips.command(description="Flip a coin")
async def flip(ctx: discord.ApplicationContext):
    res = random.choice(coins)
    embed = discord.Embed(title=res)
    await ctx.respond(embed=embed)

@coinflips.command(description="Flip multiple coins")
async def flipmore(ctx: discord.ApplicationContext):
    await ctx.respond("")

# run bot with bot token
bot.run(os.getenv("TOKEN"))