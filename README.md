# zenyth-framework
Simple Discord bot framework

## Example module
```python
class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hey(self, ctx):
        await ctx.channel.send("Hello from the example module!")

    @commands.command()
    async def ping(self, ctx):
        await ctx.channel.send("pong")

def setup(bot):
    bot.add_cog(Example(bot))
```
Use `_` as the first character in the filename of the module if you do not want it to be automatically loaded by Zenyth.
