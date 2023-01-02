import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv

from help_cog import help_cog
from music_cog import music_cog

intents = discord.Intents.all()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

bot.remove_command('help')

load_dotenv()


async def setup(bot):
    await bot.add_cog(music_cog(bot))
    await bot.add_cog(help_cog(bot))


asyncio.run(setup(bot))
bot.run(os.getenv("TOKEN"))
