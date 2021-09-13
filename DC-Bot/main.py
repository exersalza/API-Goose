import os
import discord
import json
from datetime import datetime

from discord_components import DiscordComponents
from discord.ext import commands

with open('config.json', 'r', encoding='utf-8') as c:
    config = json.load(c)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=config.get('PREFIX'), intents=intents,
                   help_command=None, description="Created by exersalza. Project: API-Goose")

DiscordComponents(bot)

for filename in os.listdir("cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f"cogs.{filename[:-3]}")

# bot.load_extension('help')
bot.run(config.get('TOKEN'))
