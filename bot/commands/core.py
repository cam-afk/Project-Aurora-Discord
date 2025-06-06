import pytz
import asyncio
from datetime import datetime
from discord.ext import commands

          
@commands.command()
async def ping(ctx):
    await ctx.send('Pong!')

@commands.command()
async def timedylon(ctx):
    
    loading_msg = await ctx.send("Calculating Dylon's time...")

    await asyncio.sleep(1)

    await ctx.message.delete()  # Delete the command message
    await loading_msg.delete()

    dylon = pytz.timezone("Europe/Paris")  # Set the timezone to Aviano - For Dylon
    now = datetime.now(dylon)
    formatted_time = now.strftime("%H:%M:%S")

    await ctx.send(f"{ctx.author.mention}, The current time for Dylon is: {formatted_time}")

@commands.command()
async def timedallas(ctx):

    await ctx.message.delete()

    central = pytz.timezone("America/Chicago") # set timezone for central america
    now= datetime.now(central)
    formatted_time = now.strftime("%H:%M:%S")

    await ctx.send(f"{ctx.author.mention}, The current time in CST is: {formatted_time}")
