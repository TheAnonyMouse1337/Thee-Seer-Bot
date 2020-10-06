import discord
import random
import  asyncio
import datetime
from discord.ext import commands
from discord.ext.commands import Cog

class Fun(commands.Cog, name="Fun"):
    
    def __init__(self, bot):
        self.bot = bot
 
#Github Challange 1
    @commands.command()
    async def guess(self, ctx):
        color = random.choice(["red","orange","yellow","lime","green","blue","cyan","purple","pink","brown","white","black"])
        await ctx.send("You only have 3 chances to guess the color! UwU!!")
        for guesses in range(1, 4):
            guess = await self.bot.wait_for('message')
            if guess.content == color:
                await ctx.send('You got it!!')
                return
            else:
                await ctx.send(f"Try: {guesses}\nNope...")
        await ctx.send(f"You Lose the color was {color}")

#Github Challenge 2
    @commands.command()
    async def math(self, ctx, arithmetic, a:int, b:int):
        if arithmetic == 'add':
            await ctx.send(a + b)
        elif arithmetic == 'sub':
            await ctx.send(a - b)
        elif arithmetic == 'mul':
            await ctx.send(a * b)
        elif arithmetic == 'div':
            await ctx.send(a / b)
        else:
            await ctx.send("Arithmetics are 'add', 'sub', 'mul', 'div'.\nTry Again UwU")
        
#Github Challange 3
    @commands.command()
    async def bmi(self, ctx, height_in_cm : int  , weight_in_Kg : int):
        height = round(float(height_in_cm) / 100, 2)
        weight = float(weight_in_Kg)
        bmi = round(weight / (height * height), 2)
        a = (f"Your body mass index is:{bmi}")
        if bmi < 18.5:
            b = 'You are underweight'
        elif 18.4 < bmi < 25:
            b = 'You are a normie'
        else:
            b = 'You are too THICC'
        await ctx.send(f"{a}\n{b}")

#Github Challenge 4
    @commands.command(aliases=["8b","8ball"])
    async def _8ball(self, ctx, *, question=None):
        if question :
            response = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "It is certain", "Most likely", "My reply is no.", "My sources say no", "Reply hazy, try again", "Signs point to yes", "Yes", "No", "Maybe"]
            await ctx.send(random.choice(response))
        else:
            await ctx.send("Where is the question dummy XD")

#OwOfy
    @commands.command(aliases=["owo"])
    async def OwO(self, ctx, *, text):
        def replace(s, old, new):
            li = s.rsplit(old, 1)
            return new.join(li)
    
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        text = text.replace('L', 'W').replace('l', 'w')
        text = text.replace('R', 'W').replace('r', 'w')
        smileys = [';;w;;', '^w^', '>w<', 'UwU', '(・`ω\´・)', '(´・ω・\`)']
        text = replace(text, '!', f'! {random.choice(smileys)}')
        text = replace(text, '?', '? owo')
        text = replace(text, '.', f'. {random.choice(smileys)}')
        for v in vowels:
            if 'n{v}'  in text:
                text = text.replace(f'n{v}', f'ny{v}')
            if 'N{V}' in text:
                text = text.replace(f'N{v}', f"N{'Y' if v.isupper() else 'y', v}")
        await ctx.send(text)
    
def setup(bot):
    bot.add_cog(Fun(bot))
    print("Fun A o K")
