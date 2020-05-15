import discord
from discord.ext import commands, tasks
import yaml
import os

config_yaml = open("config.yaml")
config = yaml.load(config_yaml, Loader=yaml.FullLoader)

bot = commands.Bot(command_prefix=str(config["command_prefix"]))


for module in os.listdir("modules"):
    if(module[0] != '_'):
        module = "modules." + module[:-3]
        bot.load_extension(module)


bot.run(str(config["token"]))
