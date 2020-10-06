import discord
import random
import datetime
from discord.ext import commands

class Info(commands.Cog, name="Information"):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def info(self, ctx,user:discord.User=None):
        if(user):
            name=f"{user.name}"
            id=f"{user.id}"
            e=discord.Embed(color=0x000000)
            e.add_field(name="Name",value=name)
            e.add_field(name="Id",value=id)
            e.set_footer(text="Made by LrnzDc")
            await ctx.send(embed=e)

    @commands.command()
    async def seek(self, ctx,user:discord.User=None):
        if 1 == 1:
            name=f"{user.name}"
            id=f"{user.id}"
            embed = discord.Embed(
                title="this *supports* a **subset** of ~~R Markdown~~",
                colour=discord.Colour(0x3b12ef),
                url="https://discord.com/",
                description="this supports [named links](https://discord.com/) on top of the subset of markdown.\nYou can use newlines too!",
                timestamp=datetime.datetime.utcfromtimestamp(1580842764) # or any other datetime type format.
            )
            embed.set_image(url="https://cdn.discordapp.com/embed/avatars/0.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/1.png")
            embed.set_author(
                name="author name",
                url="https://discord.com/", 
                icon_url="https://cdn.discordapp.com/embed/avatars/2.png"
            )
            embed.set_footer(
                text="footer text",
                icon_url="https://cdn.discordapp.com/embed/avatars/3.png"
            )
            
            embed.add_field(
                name="field title",
                value="some of these properties have different limits."
            )
            embed.add_field(
                name="another field title",
                value="try exceeding some of them! (coz idk them)"
            )
            embed.add_field(
                name=":thinking: this supports emotes! (and custom ones too)",
                value="if you exceed them, the error will tell you which value exceeds it."
            )
            embed.add_field(
                name="Inline",
                value="these last two fields",
                inline=True
            )
            embed.add_field(
                name="Fields",
                value="are inline fields",
                inline=True
            )
            
            await ctx.send(content="This is a normal message to be sent alongside the embed",embed=embed)
    
def setup(bot):
    bot.add_cog(Info(bot))
    print("Info A o K")
        