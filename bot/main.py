# Project Aurora - A Discord Bot for the Aurora Community

import discord
from discord.ext import commands

import pytz
from datetime import datetime

from commands import core  # import your custom commands

import asyncio
from dotenv import load_dotenv # grabs token
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN") # defines token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Register your commands AFTER bot is defined
bot.add_command(core.ping)
bot.add_command(core.timedylon)
bot.add_command(core.timedallas)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

bot.run(TOKEN)
