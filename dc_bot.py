from discord.ext import commands
import discord,json,os,logging

with open('./json/setting.json',mode='r',encoding="utf8") as jfile:
    jdata=json.load(jfile)

bot=commands.Bot(command_prefix='!',help_command=None,intents=discord.Intents.all())

#set up logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# if bot run, print bot is running and print cog loaded after loading all the cogs
@bot.event
async def on_ready():
    print("bot is running")

# cog load
@bot.slash_command()
@commands.is_owner()
async def load(ctx:discord.ApplicationContext,extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.respond(f'Loaded {extension} done.')
    
# cog reload
@bot.slash_command()
@commands.is_owner()
async def reload(ctx:discord.ApplicationContext,extension):
    bot.reload_extension(f'cogs.{extension}')
    await ctx.respond(f'Reloaded {extension} done.')

# cog unload
@bot.slash_command()
@commands.is_owner()
async def unload(ctx:discord.ApplicationContext,extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.respond(f'Unloaded {extension} done.')

#load all cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        try:
            bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'已加載{filename}')
        except Exception as e:
            print(f'加載{filename}時發生錯誤')
            print(e)
   
# if this profile is the main profile, run the code below
if __name__ == '__main__':
    bot.run(jdata['token'])