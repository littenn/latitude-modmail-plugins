import discord
import typing
import re
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

@client.command
async def hi(ctx, *, text=''):
    if text == '':
        ctx.send("hi")
        
        
def setup(bot):
    bot.add_cog(helloplugin(bot))

