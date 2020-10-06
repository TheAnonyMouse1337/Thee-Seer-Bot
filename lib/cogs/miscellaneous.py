import asyncio
import random
import datetime
from typing import Union
import discord
from discord.ext import commands

class Misc(commands.Cog, name="Miscellaneous"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx, *, user: Union[discord.Member, FetchedUser] = None):
        """Shows info about a user."""

        user = user or ctx.author
        if ctx.guild and isinstance(user, discord.User):
            user = ctx.guild.get_member(user.id) or user

        e = discord.Embed()
        roles = [role.name.replace('@', '@\u200b') for role in getattr(user, 'roles', [])]
        shared = sum(g.get_member(user.id) is not None for g in self.bot.guilds)
        e.set_author(name=str(user))

        def format_date(dt):
            if dt is None:
                return 'N/A'
            return f'{dt:%Y-%m-%d %H:%M} ({time.human_timedelta(dt, accuracy=3)})'

        e.add_field(name='ID', value=user.id, inline=False)
        e.add_field(name='Servers', value=f'{shared} shared', inline=False)
        e.add_field(name='Joined', value=format_date(getattr(user, 'joined_at', None)), inline=False)
        e.add_field(name='Created', value=format_date(user.created_at), inline=False)

        voice = getattr(user, 'voice', None)
        if voice is not None:
            vc = voice.channel
            other_people = len(vc.members) - 1
            voice = f'{vc.name} with {other_people} others' if other_people else f'{vc.name} by themselves'
            e.add_field(name='Voice', value=voice, inline=False)

        if roles:
            e.add_field(name='Roles', value=', '.join(roles) if len(roles) < 10 else f'{len(roles)} roles', inline=False)

        colour = user.colour
        if colour.value:
            e.colour = colour

        if user.avatar:
            e.set_thumbnail(url=user.avatar_url)

        if isinstance(user, discord.User):
            e.set_footer(text='This member is not in this server.')

        await ctx.send(embed=e)

#    @commands.command(aliases=["whois"])
#    async def userinfo(self, ctx, member: discord.Member = None):
#        if not member:  # if member is no mentioned
#            member = ctx.message.author  # set member as the author
#        roles = [role for role in member.roles]
#        embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
#                              title=f"User Info - {member}")
#        embed.set_thumbnail(url=member.avatar_url)
#        embed.set_footer(text=f"Requested by {ctx.author}")
#    
#        embed.add_field(name="ID:", value=member.id)
#        embed.add_field(name="Display Name:", value=member.display_name)
#    
#        embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
#        embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
#    
#        embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
#        embed.add_field(name="Highest Role:", value=member.top_role.mention)
#        print(member.top_role.mention)
#        await ctx.send(embed=embed)
        @commands.command()
        async def modify(ctx):
            member = ctx.message.author
            role = discord.utils.get(member.server.roles, name="My Alts")
def setup(bot):
    bot.add_cog(Misc(bot))
    print("Miscellaneous A o K")
