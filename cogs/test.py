import discord
from discord.commands import Option, slash_command
from discord.ext import commands

class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="this is a test")
    async def test(self,ctx):
        await ctx.respond("hello",ephemeral=True)

def setup(bot):
    bot.add_cog(test(bot))