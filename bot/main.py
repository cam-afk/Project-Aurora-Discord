# Project Aurora - A Discord Bot for the Aurora Community
# Bot made by camps

import discord
from discord.ext import commands

import pytz
from datetime import datetime

from commands import core  # import your custom commands 
from commands import agents # import agents from commands folder
from commands import nealinsults

import asyncio
from dotenv import load_dotenv # grabs token
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN") # defines token
SERVER = os.getenv("ID")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

# Register your commands AFTER bot is defined
bot.add_command(core.ping)
bot.add_command(core.timedylon)
bot.add_command(core.timedallas)
bot.add_command(core.trun)
bot.add_command(core.valrandom)
bot.add_command(core.insult)
bot.add_command(core.timezulu)

GUILD_ID = discord.Object(id=SERVER)

@bot.event
async def on_ready():
    await bot.load_extension("commands.core")  # First load the cog
    await bot.tree.sync(guild=GUILD_ID)        # Then sync the slash commands
    print(f'Logged in as {bot.user.name}')
    print('we online mf!')


bot.run(TOKEN)
