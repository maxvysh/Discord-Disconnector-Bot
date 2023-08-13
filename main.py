import discord
import time

TOKEN = 'REDACTED'
GUILD_ID = 'REDACTED'
USER_ID = 'REDACTED'

# Create a list of intents that includes the `guilds` and `voice_states` intents

# Pass the intents parameter when creating the client object
client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, id=int(GUILD_ID))
    member = discord.utils.get(guild.members, id=int(USER_ID))
    voice_channel = member.voice.channel
    i = 0
    n = 1
    while i <= n:
        if voice_channel is not None:
            await member.edit(voice_channel = None)
            time.sleep(1)

client.run(TOKEN)