import asyncio
import discord
import datetime
from discord.ext import commands

logs = 749838682265092167
mod_logs = 749838529126989898
auto_mod_logs = 749838473330163763
darkblue = 0x1B2738
blue = 0x74BFFF

class Logs(commands.Cog, name="Logs"):

    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        count = datetime.datetime.utcnow() - member.created_at
        milisec = count.seconds
        second = milisec // 60
        minute = second // 60
        minutes = second % 60
        hour = minute // 60
        hours = minute % 60
        day = hour // 24
        days = hour % 24
        month = day // 30.147
        months = day % 30.147
        year = month // 12

        embed = discord.Embed(
        title="A Member has Joined OwO",
        color=blue,
        timestamp=member.joined_at
        )
        
        embed.set_author(
        name=member, icon_url=member.avatar_url
        )
        
        embed.set_thumbnail(
        url=member.avatar_url
        )
        
        embed.add_field(
        name="User", value=member.mention
        )
        
        embed.add_field(
        name="Id", value=member.id
        )
        
        embed.add_field(
        name="Time on Discord:",
        value=f"{minutes}Mins {hours}Hours {days}Days {months}Months {year}Years"
        )
        
        embed.set_footer(
        text="Thee Seer 0.69", icon_url=self.bot.user.avatar_url
        )
        
        channel = self.bot.get_channel(logs)
        await channel.send(member.mention, embed=embed)
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        
        count = datetime.datetime.utcnow() - member.joined_at
        milisec = count.seconds
        second = milisec // 60
        minute = second // 60
        minutes = second % 60
        hour = minute // 60
        hours = minute % 60
        day = hour // 24
        days = hour % 24
        month = day // 30.147
        months = day % 30.147
        year = month // 12
        
        embed = discord.Embed(
        title="A Member has Left UwU",
        color=darkblue,
        timestamp=member.joined_at
        )
        
        embed.set_author(
        name=member,
        icon_url=member.avatar_url
        )
        
        embed.set_thumbnail(
        url=member.avatar_url
        )
        
        embed.add_field(
        name="User", value=member.mention
        )
        
        embed.add_field(
        name="Id", value=member.id
        )
        
        embed.add_field(
        name="Time on Server:",
        value=f"{minutes}Mins {hours}Hours {days}Days {months}Months {year}Years"
        )
        
        embed.set_footer(
        text="Thee Seer 0.69", icon_url=self.bot.user.avatar_url
        )
        
        channel = self.bot.get_channel(logs)
        await channel.send(member.mention, embed=embed)

def setup(bot):
    bot.add_cog(Logs(bot))
    print("Logs A o K")
