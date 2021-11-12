import discord
from discord.ext import commands
from discord.ext.commands import cog

client = commands.Bot(command_prefix="!")
client.remove_command("help")

cog_files = []
f = open("cogs.txt", "r")
for x in f:
    if x[-1:] == "\n":
        x = x[:-1]
    cog_files.append(x)

for cog in cog_files:
    client.load_extension(cog)
    print("%s has loaded." % cog)

token = open(r"token.txt").read()

client.run(token)