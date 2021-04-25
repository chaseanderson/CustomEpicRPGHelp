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
    
    #print(message.channel)
    #print(message.content)

    if(str(message.channel) == 'epicrpg'):
      #print('epicrpg channel')
      s = message.content

      print(message.author)
      print(message.content)

      if s.find('EPIC GUARD') != -1 and s.find('stop there') != -1:
        print('epic guard')
        s=s.replace('!', '')
        memberID = s[s.find('@', 0, len(s))+1: s.find('>', 0, len(s))] #get the user mention in the message
        print('member id: ' + str(memberID))
        user = message.guild.get_member(int(memberID))
        role = message.guild.get_role(834995449949061141)
        await message.channel.send("get neigh neighed, kid")
        await user.remove_roles(role)
        print('role removed')
        #await message.channel.send("get neigh neighed, kid")

    if(str(message.channel) == 'epicrpg-jail'):
      if(str(message.content) == 'i am a cheater'):
        role = message.guild.get_role(834995449949061141)
        await message.author.add_roles(role)

        print("role added")
    if message.content == 'raise-exception':
        raise discord.DiscordException

client.run(TOKEN)