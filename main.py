import os
import discord

client = discord.Client()
TOKEN = os.environ['TOKEN']

@client.event
async def on_ready():
  print('Rymu is ready, what do you need? {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('=hello'):
    await message.channel.send('hello there young traveler')

client.run(TOKEN)



