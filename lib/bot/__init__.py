
from asyncio import sleep
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
from discord.ext.commands import Bot as Seer
import discord
from glob import glob

from discord.ext.commands import (CommandNotFound,
BadArgument,
MissingRequiredArgument, CommandOnCooldown)

from ..db import db
import os 
from apscheduler.triggers.cron import CronTrigger

PREFIX = "s!"
OWNER_IDS = [734103977288794232]
COGS = ['fun',"logs","moderation","info","ascii"]
IGNORE_EXCEPTIONS = (CommandNotFound, BadArgument)
print(COGS)

class Ready(object):
    def __init__(self):
        for cog in COGS:
            setattr(self, cog, False)
    
    def ready_up(self, cog):
        setattr(self, cog, True)
        print(f" {cog} cog ready")
    
    def all_ready(self):
        return all([getattr(self, cog) for cog in COGS])

class Bot(Seer):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = [748393173167898636]
        self.cogs_ready = Ready()
        self.scheduler = AsyncIOScheduler()

        db.autosave(self.scheduler)
        super().__init__(command_prefix = PREFIX, owner_ids = OWNER_IDS)
    
    def setup(self):
        for cog in COGS:
            self.load_extension(f'lib.cogs.{cog}')
            print(f'{cog} cog loaded')
        print('setup complete')

    def run(self, version):
        self.VERSION = version
        print("running setup")
        self.setup()
        self.member = 760126281521037353

        with open("./lib/bot/token.txt") as op:
            self.TOKEN = op.read()

        print("running bot...")
        super().run(self.TOKEN,reconnect=True)
    
    async def print_message(self):
        self.stdout.send(embed = discord.Embed(title = "Good Morning!",colour = discord.Colour.orange()))

    async def on_connect(self):
        print("Bot connected")
    
    async def on_disconnect(self):
        print("bot disconnected")
    
    async def on_error(self, err, *args, **kwargs,):
        if err == "on_command_error":
            await args[0].send("Something went wrong")
        embed = discord.Embed(title = "An error occured", colour = discord.Colour.red(),timestamp = datetime.utcnow())
        await self.stdout.send(embed = embed)
        raise

    async def on_command_error(self,ctx,exc):
        if isinstance(exc,CommandNotFound):
            await ctx.send(embed = discord.Embed(title = "  Can't find command '_' ", colour = discord.Colour.red()))
        elif isinstance(exc, BadArgument):
            pass
        elif isinstance(exc,CommandOnCooldown):
            await ctx.send(embed = discord.Embed(title = f"That command is on {str(exc.cooldown.type).split('.')[-1]} cooldown. Try again in {exc.retry_after:,.2f}", colour = discord.Colour.red()))
        elif isinstance(exc, MissingRequiredArgument):
            await ctx.send("One or two required arguments are missing")
        else:
            raise exc.original
    
    async def on_ready(self):
        if not self.ready:
            self.guild = self.get_guild(748393173167898636)
            self.scheduler.add_job(self.print_message,CronTrigger(day_of_week = 0, hour=12,minute = 0, second=0))
            self.scheduler.start()
            self.stdout = self.get_channel(749838682265092167)
            embed = discord.Embed(title = "Bot is Online",
            colour = discord.Colour.purple(),timestamp = datetime.utcnow())
            embed.set_author(name=self.guild.name,icon_url=self.guild.icon_url)
           
            while not self.cogs_ready.all_ready():
                await sleep(0.5)
            self.ready = True
            await self.stdout.send(embed = embed)
            print("Bot ready")
        else:
            print("Bot reconnected")
    async def on_message(self, message):
        if not message.author.bot:
            await self.process_commands(message)

bot = Bot()