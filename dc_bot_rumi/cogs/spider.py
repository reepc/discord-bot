from discord.ext import commands
from core.classes import Cog_Extension
from requests import HTTPError
from urllib.parse import urlencode
import requests as req
import random as ran
import json,asyncio,discord,re

with open('./json/setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

session=req.session()
    
class pixiv(Cog_Extension):
    
            
    proxies={
    'http':'http://127.0.0.1:51837',
    'https':'https://127.0.0.1:51837'
    }         

    headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "refer": "https://www.pixiv.com/",
    'PHPSESSID':jdata['PHPSESSID'],
    }
    
    #group the commands below
    @commands.group()
    async def pixiv(self,ctx):
        self.length=len('pixiv')
    
    #send a random picture on pixiv that is not R18
    @pixiv.command()
    async def normal(self,ctx):
        channel=int(jdata['pic_channel'])
        
        params1={
            'keyword':{ctx.message.content[(self.length+9):]},
            'tags':[],
            'PHPSESSID':'58770492_0nN7Hsu3YFvdln5wjqkPLdye9DGLWN6x'
        }
        
        self.message=ctx.message.content[self.length+9:]
        
        global false, null, true
        false='False'
        null='None'
        true='True'
        
        rn=ran.randint(1000000,200000000)
        
        if ctx.channel.id==channel:
            url=f'https://www.pixiv.net/ajax/illust/{rn}'
            request=req.get(url)
            response_1=session.get(url)
            response_1=eval(response_1.content)['body']
            
            """ while request.status_code!=200:
                url=f'https://www.pixiv.net/ajax/illust/{rn}'
                request=req.get(url)
                response_1=session.get(url)
                response_1 = eval(response_1.content)['body'] """
                
            r18=True
            
            while request.status_code!=200 and r18==True:
                rn=ran.randint(1000000,200000000)
                url=f'https://www.pixiv.net/ajax/illust/{rn}'
                request=req.get(url)
                response_1=session.get(url)
                response_1=eval(response_1.content)['body']
                
                if request.status_code==200:
                    params1['tags'].clear()
                    for tag in response_1['tags']['tags']:
                        params1['tags'].append(tag['tag'])
                else:
                    continue
                
                if 'R18' in params1['tags']:
                    r18=True
                else:
                    r18=False
                    pic_url=f'https://www.pixiv.net/artworks/{rn}'
                    ctx.send(pic_url)
                
                await asyncio.sleep(0.1)
                
        else:
            await ctx.send("你不在抓圖頻道")
    
    #not finished, send a message that is r18 picture
    @pixiv.command()
    async def R18(self,ctx):
        param2={
            'character':{ctx.message.content[self.length+4:]},
            'PHPSESSID':'58770492_0nN7Hsu3YFvdln5wjqkPLdye9DGLWN6x'
        }
        
        self.message=param2['character']
        rn=ran.randint(1000000,200000000)
        
        if ctx.channel.is_nsfw():
            url=f'https://www.pixiv.net/artworks/{rn}'
            request=req.get(url)
            response_1=req.session(url)
            while request.status_code!=200 and self.message not in response_1['tag']:
                url=f'https://www.pixiv.net/artworks/{rn}'
                request=req.get(url)
            await ctx.send(url)
        else:
            await ctx.send('this is now a nsfw channel') 
            
    #to search picture with the keyword user input and return the url of the picture that searched on pixiv
    @pixiv.command()
    async def search(self,ctx):
        
        global false, null, true
        false = 'False'
        null = 'None'
        true = 'True'
        
        if ctx.channel.id==int(jdata['sever_210']['pic_channel']) or ctx.channel.id==int(jdata['sever_107']['pic_channel']):
            try:
                url=f'https://www.pixiv.net/ajax/search/artworks/{ctx.message.content[self.length+9:]}?'
                session=req.session()
                response_1=session.get(url)
                response_1=eval(response_1.content)['body']['illustManga']['data']
                datas=response_1
                pic_id=[]
                
                for data in datas:
                    if 'id' in data:
                        pic_id.append(data['id'])
            

                random_choice=ran.choice(pic_id)
                pic_url=f'https://www.pixiv.net/artworks/{random_choice}'
                embed_url=f'https://pixiv.cat/{random_choice}.jpg'
                
                
                embed=discord.Embed(title="Here's yout picture url and picture",description=pic_url,color=discord.Color.random())
                embed.set_author(name=f'{self.bot.user}',icon_url=jdata['icon_url_for_embed'])
                embed.set_footer(text=f'bot and embed made by reep_c#3507')
                embed.set_image(url=embed_url)
                await ctx.send(embed=embed)
                pic_id.clear()
            
            except HTTPError as error:
                raise error
        
        else:
            ctx.send('Not in the correct channel')
                    
        
async def setup(bot):
    await bot.add_cog(pixiv(bot))