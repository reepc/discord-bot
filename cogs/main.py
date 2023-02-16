from discord.ext import commands
from core.classes import Cog_Extension
from discord.commands import slash_command
from discord import errors
import json,discord

with open('./json/setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)
    


class main(Cog_Extension):

    # print bot ping
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f"{round(self.bot.latency*1000)}(ms)")
    
    @slash_command(description='delete the messages')
    @discord.default_permissions(administrator=True)
    async def purge(self,ctx:discord.ApplicationContext,num:int):
        await ctx.channel.purge(limit=num+1)
        await ctx.respond('delete complete')
        
# set up the cog to the bot
def setup(bot):
    bot.add_cog(main(bot))