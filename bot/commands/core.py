import pytz
import asyncio
import random
import discord
import os
from datetime import datetime
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from . import agents  # from the same folder import agents
from . import nealinsults # same as above

load_dotenv()
USER = os.getenv("USER")
SERVER = os.getenv("ID")

GUILD_ID = discord.Object(id=SERVER)

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

@commands.command()
async def timezulu(ctx):
        await ctx.message.delete()

        zulu = pytz.timezone("Canada/Atlantic") #timezone for nathan "canadianzulu "
        now = datetime.now(zulu)
        formatted_time = now.strftime("%H:%M")

        await ctx.send(f"{ctx.author.mention}, The current time for Zulu is: {formatted_time}")

### literally to make sure im running from terminal and not docker

@commands.command()
async def trun(ctx):
    await ctx.message.delete()

    await ctx.send(f'Hey {ctx.author.mention}, were now running from the terminal!!')

@commands.command()
async def valrandom(ctx):
    await ctx.message.delete()

    random_agent = random.choice(agents.agent_list) 

    await ctx.send(f"{ctx.author.mention}, Looks like you gotta play {random_agent} 😭")



class ValButton(discord.ui.View): #creates a class called ValButton that subclasses discord.ui.View
    @discord.ui.button(label="Choose an Agent!", style=discord.ButtonStyle.primary) # create a  button with a emoji label that says "Choose an Agent!" with color burple 
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        random_agent = random.choice(agents.agent_list)
        await interaction.response.send_message(f"{interaction.user.mention}, Looks like you have to play {random_agent}!")
            

### first class and slash command            

class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @app_commands.command(name="valrandom", description = "Get a random agent for your next game!!")
    @app_commands.guilds(GUILD_ID)
    async def RandomAgent(self, interaction: discord.Interaction):
        print("Slash command triggered")
        await interaction.response.send_message("CHOOSE YOUR SWIFTPLAY FATE!", view = ValButton())

async def setup(bot):
    await bot.add_cog(Core(bot))

@commands.command()
async def insult(ctx, member: discord.Member = None ):
    await ctx.message.delete()

    if member is None:
        member = await ctx.bot.fetch_user(USER)
    
    insult_line = random.choice(nealinsults.neal_insults)
    await ctx.send(f"{member.mention}, {insult_line}")




    #### @commands.command()
#async def insultneal(ctx):
    #await ctx.message.delete()
    #neal = await ctx.bot.fetch_user(493662983147356160)
    #nealinsult = random.choice(nealinsults.neal_insults)
    #await ctx.send(f"{neal.mention}, {nealinsult}")
