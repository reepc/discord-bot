from email import message
from discord.ext import commands
from core.classes import Cog_Extension
import json,random,datetime,discord

with open('./json/setting.json',mode='r',encoding="utf8") as jfile:
    jdata = json.load(jfile)
    
class event(Cog_Extension):

    # auto reply messenger send author if they send message include sentence below
    """ @commands.Cog.listener()
    async def on_message(self,ctx):
        keyword=[-1,'幹','靠北','哭啊']
        return_word=[-1,"幹三小","靠北三小 你爸死了哦","乖別哭 越哭越像豬"]
        for i in range(len(keyword)):
            i+=1
            if ctx.author==self.bot.user or i>=len(keyword):
                return
            elif ctx.content in keyword[i]:
                await ctx.channel.send(return_word[i])        
    
    # members join   
    @commands.Cog.listener() 
    async def on_member_join(self,member):
        channel=self.bot.get_channel(int(jdata["join_channel"]))
        await channel.send(f"{member.mentioned} join")
    
    # members leave
    @commands.Cog.listener() 
    async def on_member_remove(self,):
        channel=self.bot.get_channel(int(jdata["leave_channel"]))
        await channel.send(f"{self.member.mention} leave")
        
    @commands.Cog.listener()
    async def on_message(self,ctx):
        if ctx.message.startswith('rumi') or ctx.message.startswith('懶貓子'):
            await ctx.channel.send(f"{ctx.author.mention} {random.choice(jdata['word'])}")
            
    @commands.Cog.listener()
    async def auto_mention_response(self,msg):
        if msg.content == self.bot.user:
            await msg.channel.send("喵好")
            
    @commands.Cog.listener()
    async def reply_to_reep(self,msg):
        if msg.author==int(jdata["reep_c"]) and msg.endswith('rumi'):
            await msg.channel.send("老公?") """
            
# set up the cog to the bot           
def setup(bot):
    bot.add_cog(event(bot))