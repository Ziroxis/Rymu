import os
import discord
from discord.ext import commands
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='.', intents=intents)
TOKEN = os.environ['TOKEN']


@client.event
async def on_ready():
    print('I am ready master, what do you need? {0.user}'.format(client))


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')


keep_alive()
client.run(TOKEN)
