import discord
from dotenv import load_dotenv
import os
import random

# load environment variables
load_dotenv()
bot = discord.Bot()

coinflips = bot.create_group("coins", "flip coins")

diceroll = bot.create_group("dice", "roll dice")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

coins = ["Heads", "Tails"]

@coinflips.command(description="Flip a coin")
async def flip(ctx: discord.ApplicationContext):
    res = random.choice(coins)
    embed = discord.Embed(title=res)
    await ctx.respond(embed=embed)

@coinflips.command(description="Flip multiple coins (1 or more)")
async def flipmore(ctx: discord.ApplicationContext, num: int):
    embed = discord.Embed(title="Invalid number of coins", description="Enter at least 1 (Max: 99999)")
    if 0 < num < 100000:
        res = 0
        for i in range(num):
            res += random.randint(0, 1)
        embed = discord.Embed(title=f'Heads: {res}, Tails: {num - res}')
    await ctx.respond(embed=embed)

@diceroll.command(description="Roll a die")
async def roll(ctx: discord.ApplicationContext, sides: int):
    embed = discord.Embed(title="Invalid number of sides", description="Enter at least 2 (Max: 99999)")
    if 1 < sides < 100000:
        embed = discord.Embed(title=f'Result: {random.randint(1, sides)}')
    await ctx.respond(embed=embed)

# run bot with bot token
bot.run(os.getenv("TOKEN"))