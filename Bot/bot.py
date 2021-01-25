import discord, json, os, base64, pathlib, asyncio
from discord.ext import commands
from BotCommands import bot_help, code_run, get_quote, get_cat, language
from BotCogs import codeCog

path = pathlib.Path(__file__).parent.absolute()
os.chdir(path)

botObj =  commands.Bot(command_prefix="pb.", help_command=None)

@botObj.command(aliases=["h"])
async def help(ctx):
	await bot_help.help(ctx)

@botObj.command()
async def quote(ctx):
	await get_quote.quote(ctx)

@botObj.command(aliases=["CATS", "cat"])
async def cats(ctx):
	await get_cat.cats(ctx)

@botObj.command(aliases=["langs", "lang"])
async def languages(ctx):
	await language.languages(ctx)

def run(bot, token):
    bot.run(token)

def setup(bot):
	bot.add_cog(codeCog.Events(bot))

with open("../config", "r") as f:
	TOKEN = base64.b64decode(bytes(f.read().strip(), "utf-8")).decode('utf-8')

if __name__ == "__main__":
	setup(botObj)
	run(botObj, TOKEN)


# https://discordpy.readthedocs.io/en/latest/api.html#discord.Message.add_reaction
