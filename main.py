import discord

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".foramt(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

client.run(MTAyMjkxNTE1MzM4NzMzNTc4NA.GsKDox.An1vhO2ecmJbTl0vtDPWE3yzLl-eFQx2ChBRcI)