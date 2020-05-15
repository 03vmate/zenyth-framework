import discord
from discord.ext import commands

class Testmodule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.channel.send("hello!")

def setup(bot):
    bot.add_cog(Testmodule(bot))

