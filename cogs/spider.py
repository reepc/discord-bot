from discord.ext import commands
from discord.commands import slash_command
from func.spiderfunc import func
from core.classes import Cog_Extension
from discord import is_nsfw
import discord,json,re

with open('./json/setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class piv(Cog_Extension):

    @slash_command(description='enter keywords to get picture in pixiv')
    async def search_picture(self,ctx:discord.ApplicationContext,message:str):
        pic_url,embed_url=func().catch_pic(keyword=message)
        pic_embed=discord.Embed(title="Here's yout picture url and picture",color=discord.Color.random(),description=pic_url)
        pic_embed.set_author(name=f'{self.bot.user}',icon_url=jdata['icon_url_for_embed'])
        pic_embed.set_footer(text=f'bot and embed made by reep_c#3507')
        pic_embed.set_image(url=embed_url)
        ephemeral=True if isinstance(ctx,discord.DMChannel) else False 
        await ctx.respond(embed=pic_embed,ephemeral=ephemeral)
    
    @slash_command(description='get random picture from pixiv')
    async def random_pic(self,ctx:discord.ApplicationContext):
        pic_url,embed_url=func().catch_pic(random=True)
        pic_embed=discord.Embed(title="Here's yout picture url and picture",description=pic_url,color=discord.Color.random())
        pic_embed.set_author(name=f'{self.bot.user}',icon_url=jdata['icon_url_for_embed'])
        pic_embed.set_footer(text=f'bot and embed made by reep_c#3507')
        pic_embed.set_image(url=embed_url)
        await ctx.respond(embed=pic_embed)       

def setup(bot):
    bot.add_cog(piv(bot))