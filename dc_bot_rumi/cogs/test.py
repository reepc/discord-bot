import discord
from discord import *
from discord.ext import commands
from discord.ui import *
from core.classes import Cog_Extension

class test(Cog_Extension):
    
    @commands.command()
    async def test5(self,ctx):
        menu=discord.ui.Select(
            placeholder="this is for server's",
            options=[
            discord.SelectOption(label='遊戲伺服器事宜',value="1"),
            discord.SelectOption(label='Discord 伺服器事宜',value="2"),
            discord.SelectOption(label='其他',value="3")
                    ]
        )
        view=View(timeout=0)
        view.add_item(menu)
        await ctx.send(view=view)
        async def m1(interaction):
            if menu.values[0]=='1':
                await interaction.response.send_message(f'you got')
            else:
                await ctx.send(f'123')
        menu.callback=m1
    
async def setup(bot):
    await bot.add_cog(test(bot))