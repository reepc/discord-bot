from discord.ext import commands
from core.classes import Cog_Extension
import  random,os,json,random,math

with open('./json/setting.json',mode='r',encoding="utf8") as jfile:
    jdata = json.load(jfile)
    
class react(Cog_Extension):
    
    # print pi
    @commands.command()
    async def pi(self,ctx):
        await ctx.send(math.pi)
    
    # print random sentence
    @commands.command()
    async def sendmessage(self,ctx):
        message=['你媽死了','?你禮貌嗎','竹林愛你','那你很厲害欸','爲什麽要這樣對我','你的同學愛呢?','沒關係，別在意','有帥哥嗎','對啦我就膚淺','好的']
        await ctx.send(random.choice(message))
        
# set up the cog to the bot        
def setup(bot):
    bot.add_cog(react(bot))