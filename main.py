import discord

client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print("We have logged in as {0.user}".foramt(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

client.run('MTAyMjkxNTE1MzM4NzMzNTc4NA.GqtR_w.XE9Dd9gAhrZUudza9Caahyo37t86GaOdKQ4qdg')