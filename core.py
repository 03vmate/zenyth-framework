import discord
from discord.ext import commands, tasks
import yaml
import os
from os import path

#Open and load config.yaml
config_yaml = open("config.yaml")
config = yaml.load(config_yaml, Loader=yaml.FullLoader)

#INTERNAL USE -- Keep track of loaded modules
loaded_modules = []

#Set up bot object and the command prefix
bot = commands.Bot(command_prefix=str(config["command_prefix"]))

#Autoload modules
for module in os.listdir("modules"):
    if(module[0] != '_'):
        loaded_modules.append(module[:-3])
        module = "modules." + module[:-3]
        bot.load_extension(module)

#Manually load modules
@bot.command()
async def load(ctx, *opt):
    for arg in opt:
        #We don't know if it's an autoloading module that was unloaded or it's a non-autoloading module, so we have to try both
        if(path.exists("modules/_" + arg + ".py") or path.exists("modules/" + arg + ".py")):
            success = 0
            try:
                bot.load_extension("modules._" + arg)
                success = 1
                loaded_modules.append(arg)
                await ctx.channel.send("Loaded " + arg)
            except:
                pass
            try:
                bot.load_extension("modules." + arg)
                success = 1
                loaded_modules.append(arg)
                await ctx.channel.send("Loaded " + arg)
            except:
                pass
            if(not success):
                await ctx.channel.send("Error loading " + arg)
        else:
            await ctx.channel.send("No extension with name " + arg)

#Unload module
@bot.command()
async def unload(ctx, *opt):
    for arg in opt:
        #We don't know if it's an autoloading module that was unloaded or it's a non-autoloading module, so we have to try both
        success = 0
        try:
            bot.unload_extension("modules._" + arg)
            success = 1
            loaded_modules.remove(arg)
        except:
            pass
        try:
            bot.unload_extension("modules." + arg)
            success = 1
            loaded_modules.remove(arg)
        except:
            pass
        if(success == 0):
            await ctx.channel.send("Error unloading extension")
        else:
            await ctx.channel.send("Unloaded " + arg)

#Reload module
@bot.command()
async def reload(ctx, *opt):
    for arg in opt:
        if(arg not in loaded_modules and "_" + arg not in loaded_modules):
            await ctx.channel.send("Extension " + arg + " is not running or doesn't exist!")
        if(arg in loaded_modules):
            bot.reload_extension("modules." + arg)
            await ctx.channel.send("Reloaded " + arg)
        if("_" + arg in loaded_modules):
            bot.reload_extension("modules._" + arg)
            await ctx.channel.send("Reloaded " + arg)

#List loaded and unloaded modules
@bot.command()
async def modules(ctx):
    embed_loaded = discord.Embed(title="Loaded modules", description="", color=0x00ff00)
    embed_unloaded = discord.Embed(title="Unloaded modules", description="", color=0xff0000)
    unloaded = []
    for module in os.listdir("modules"):
        if("__pycache__" not in module and "__init__" not in module):
            unloaded.append(module[:-3])
    for module in loaded_modules:
        unloaded.remove(module)
        embed_loaded.add_field(name="modules/", value=module, inline=True)
    for module in unloaded:
        embed_unloaded.add_field(name="modules/", value=module, inline=True)
    await ctx.channel.send(embed=embed_loaded)
    await ctx.channel.send(embed=embed_unloaded)

bot.run(str(config["token"]))

