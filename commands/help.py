import discord
from discord.ext import commands

class Reaction(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="help")
    async def help(self, ctx: commands.Context, *, args: str = None):
        embed = discord.Embed(title='Help:')
        embed.add_field(name='!reaction [TEXT]', value='It gives you a image related to the text you put in.', inline=False)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Reaction(client))