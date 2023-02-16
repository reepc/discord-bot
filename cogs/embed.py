from discord.ext import commands
from core.classes import Cog_Extension
import json,discord

with open('./json/setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)
    
class embed(Cog_Extension):
    
    @commands.command()
    async def embed(self,ctx):
        pass

def setup(bot):
    bot.add_cog(embed(bot))
        