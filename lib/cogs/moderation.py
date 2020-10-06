import discord
import random
import datetime
from discord.ext import commands

class Mod(commands.Cog, name="Moderation"):
    
    def __init__(self, bot):
        self.bot = bot
        self.guild = 748393173167898636

    @commands.command()
    async def clear(self, ctx, amount : int):
    	await ctx.channel.purge(limit=amount)
    	
    @commands.command()
    async def ban (self, ctx, member:discord.User=None, reason =None):
        if member == None or member == ctx.message.author:
            await ctx.channel.send("You cannot ban yourself")
            return
        if reason == None:
            reason = "Server Dead"
        message = f"You have been banned from {ctx.guild.name} for {reason}"
        await ctx.guild.ban(member, reason=reason)
        await ctx.channel.send(f"{member} is banned!")
        
    @commands.command()
    async def add_role(self, ctx):
        member = ctx.author
        role = discord.utils.get(member.guild.roles, name="Stalker")
        await discord.Member.add_roles(member, role)
    	
def setup(bot):
    bot.add_cog(Mod(bot))
    print("Moderation A o K")
