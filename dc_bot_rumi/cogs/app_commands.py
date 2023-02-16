import discord 
from discord.ext import commands
from discord import app_commands
from core.classes import Cog_Extension

class slash(Cog_Extension,):
    

    @app_commands.command(name='test',description='test from')
    async def test(self,interaction,test:str):
        await interaction.response.send_message('opas')
        
async def setup(bot:commands.Bot):
   await bot.add_cog(slash(bot))

async def setup_hook(self):
    await app_commands.CommandTree.sync(self)