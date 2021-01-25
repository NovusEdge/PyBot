import discord
from discord.ext import commands
import requests, json, asyncio
from BotCommands import code_run

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready!')
        print('Logged in as ---->', self.bot.user)
        print('ID:', self.bot.user.id)

    #
    # @commands.Cog.listener()
    # async def on_reaction_add(self, reaction, user):
    #     print("REACTION!!")
    #     msg = reaction.message.content
    #     if not user.bot and msg.startswith("```"):
    #         print("REACTION!!")
    #         if reaction.emoji == "⚡":
    #             await code_run.runcode(reaction, user)
