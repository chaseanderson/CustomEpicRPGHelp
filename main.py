import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_NAME')
chunk_guilds_at_startup =True
fetch_offline_members=True

#client = discord.Client()
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
  if message.author == client.user:
      return

  if(str(message.channel) == 'epicrpg'):
    await epicrpg_channel(message)
  elif(str(message.channel) == 'admin-training'):
    await epicrpg_jail_channel(message)

  if message.content == 'raise-exception':
    raise discord.DiscordException

#Different Channel Commands
async def epicrpg_channel(message):
  s = message.content
  #if the bot says so
  if(message.author.bot and str(message.author) == 'EPIC RPG#4117' and (s.find('EPIC GUARD') != -1 and s.find('stop there') != -1)):
    s=s.replace('!', '')
    memberID = s[s.find('@', 0, len(s))+1: s.find('>', 0, len(s))] #get the user mention in the message
    user = message.guild.get_member(int(memberID))
    role = message.guild.get_role(834995449949061141)
    await message.channel.send("get neigh neighed, kid")
    await user.remove_roles(role)
  
async def epicrpg_jail_channel(message):
  if(str(message.content) == 'i am a cheater'):
    role = message.guild.get_role(834995449949061141)
    await message.author.add_roles(role)

client.run(TOKEN)
