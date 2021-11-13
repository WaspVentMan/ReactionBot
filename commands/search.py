from simple_image_download import simple_image_download as simp
import discord
from discord.ext import commands
import random
import os
import shutil

class Reaction(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="reaction")
    async def help(self, ctx: commands.Context, *, args: str = None):
        n = random.randint(1,10)
        m = await ctx.send("Downloading Images...")
        try:
            parameters = args.replace(" ", "_")
        except:
            await m.edit(content="An error occured.")
        response = simp.simple_image_download
        response().download(parameters, 10)
        dir = os.listdir("simple_images/" + parameters)
        try:
            file = discord.File("simple_images/" + parameters + "/" + dir[n])
        except:
            await m.delete()
            await ctx.send(content="An error occured.")
            return
        await m.edit(content="Sending...")
        await ctx.send(file=file)
        await m.delete()
        shutil.rmtree("simple_images")

def setup(client):
    client.add_cog(Reaction(client))