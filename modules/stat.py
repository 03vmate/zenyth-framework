import discord
from discord.ext import commands
import datetime
initdate = datetime.datetime.now()
class Stat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stat(self, ctx):
        uptime = datetime.datetime.now() - initdate
        await ctx.channel.send("Bot uptime is " + str(uptime))

def setup(bot):
    bot.add_cog(Stat(bot))

