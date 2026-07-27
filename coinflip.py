import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# retrieve bot token form file
f = open("token.txt")
token = f.read()
f.close()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# place a bot token here
client.run(token)