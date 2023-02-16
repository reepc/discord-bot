import discord
from discord.ext import commands
import json,datetime
from youtube_dl import YoutubeDL

class Cog_Extension(commands.Cog):
    """用於Cog繼承基本屬性"""
    def __init__(self,bot:commands.Bot):
        self.bot=bot
        self.guild=discord.Guild
        self.member=discord.Member
    
        self.is_playing=False
        self.is_paused=False
        
        self.music_queue=[]
        self.YDL_OPTIONS={'format':'bestaudio','noplaylist':'True'}
        self.FFMPEG_OPTIONS={'before_options':'-reconnect 1 -reconnected_streamed 1 -reconnect_delay_max 5','options':'-vn'}
        
        self.vc=None