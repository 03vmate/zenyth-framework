from discord.ext import commands

@commands.command()
async def helloworld(ctx):
    await ctx.channel.send("hello!")

def setup(bot):
    bot.add_command(helloworld)