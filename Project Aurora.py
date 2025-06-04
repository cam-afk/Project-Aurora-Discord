# Project Aurora - A Discord Bot for the Aurora Community

import discord  
from discord.ext import commands

import pytz
from datetime import datetime
# Define the timezone for the bot

import asyncio

# Define the bot's command prefix and intents
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent

from dotenv import load_dotenv # loads env structure
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN") # Grabs token from .env file 

###############################


bot = commands.Bot(command_prefix='!', intents=intents) 

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
          
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def timedylon(ctx):
    
    loading_msg = await ctx.send("Calculating Dylon's time...")

    await asyncio.sleep(2)

    await ctx.message.delete()  # Delete the command message
    await loading_msg.delete()

    dylon = pytz.timezone("Europe/Paris")  # Set the timezone to Aviano - For Dylon
    now = datetime.now(dylon)
    formatted_time = now.strftime("%H:%M:%S")

    await ctx.send(f"{ctx.author.mention}, The current time for Dylon is: {formatted_time}")

@bot.command()
async def timedallas(ctx):

    await ctx.message.delete()

    central = pytz.timezone("America/Chicago") # set timezone for central america
    now= datetime.now(central)
    formatted_time = now.strftime("%H:%M:%S")

    await ctx.send(f"{ctx.author.mention}, The current time in CST is: {formatted_time}")

bot.run(TOKEN)