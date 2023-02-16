from discord.ext import commands
from core.classes import Cog_Extension
import requests as req
import discord
import json

with open('./json/setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class help_command(Cog_Extension):
    
    @commands.command()
    async def help(self,ctx):
        embed=discord.Embed(title="Here's all the commands",color=discord.Color.random())
        embed.set_author(name=f'{self.bot.user}',icon_url=jdata["icon_url_for_embed"])
        embed.add_field(name='The things this bot can do',value='search the picture which have the keyword you sent on\nsend some response if you said something or your sentence start with some keyword\n',inline=False)
        embed.add_field(name='command',value="ping:show the bot's latency\npurge:clean the message(you need to enter how many message you want to clean)\ninterval:update the sever total member number in the top voice channel")
        embed.add_field(name='pixiv command',value='normal:send a random picture on pixiv\nR18:send a R18 picture\nsearch:send the picture that have the keyword you send')
        embed.add_field(name='please note',value="the pixiv command can just send a R18 picture in nsfw channel\n purge,interval and ping command can only use by the admin",inline=False)
        embed.set_footer(text=f'bot and embed made by reep_c#3507')
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(help_command(bot))