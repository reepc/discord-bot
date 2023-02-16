from discord.ext import commands
import discord,json,os
from discord import app_commands

with open('./json/setting.json',mode='r',encoding="utf8") as jfile:
    jdata=json.load(jfile)

bot=commands.Bot(command_prefix="!",owner_id=544070742078259200,help_command=None,intents=discord.Intents.all())

# if bot run, print bot is running and print cog loaded after loading all the cogs
@bot.event
async def on_ready():
    print("bot is running")
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
    print('cogs loaded successfully')
    
    
# test it can or can't normally run 
@bot.command()
async def t(ctx):
    all_member=ctx.guild.member_count
    print(all_member)
    
@bot.command()
async def t2(ctx):
    data={
        "1":"a",
        "2":"b"
        }
    with open(f"./json/{ctx.guild.id}.json",mode='w') as jsondata:
        json.dump(data,jsondata)
       
# cog load
@bot.command()
@commands.is_owner()
async def load(ctx,extension):
    await bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded {extension} done.')
    
# cog reload
@bot.command()
@commands.is_owner()
async def reload(ctx,extension):
    await bot.reload_extension(f'cogs.{extension}')
    await ctx.send(f'Reloaded {extension} done.')

# cog unload
@bot.command()
@commands.is_owner()
async def unload(ctx,extension):
    await bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded {extension} done.')
    
        
# if this profile is the main profile, run the code below
if __name__ == '__main__':
    bot.run(jdata['token'])