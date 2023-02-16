from discord.ext import commands
from core.classes import Cog_Extension
import json,asyncio,discord,re

with open('./json/setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)
    


class main(Cog_Extension):

    # print bot ping
    """ @commands.command()
    async def ping(self,ctx):
        await ctx.send(f"{round(self.bot.latency*1000)}(ms)") """
    
    @commands.command()
    async def purge(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)
        
# set up the cog to the bot
async def setup(bot):
    await bot.add_cog(main(bot))