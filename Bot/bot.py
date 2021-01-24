import discord, json, os, base64, pathlib, asyncio
from discord.ext import commands
from BotCommands import bot_help, code_run, get_quote, get_cat
from BotCogs import *

path = pathlib.Path(__file__).parent.absolute()
os.chdir(path)

botObj =  commands.Bot(command_prefix=">", help_command=None)

@botObj.event
async def on_ready():
	print('Bot Running')

@botObj.command(aliases=["h"])
async def help(ctx):
	await bot_help.help(ctx)

@botObj.command()
async def quote(ctx):
	await get_quote.quote(ctx)

@botObj.command(aliases=["CATS"])
async def cats(ctx):
	await get_cat.cats(ctx)


def run(bot, token):
    bot.run(token)

with open("../config", "r") as f:
    TOKEN = base64.b64decode(bytes(f.read().strip(), "utf-8")).decode('utf-8')

if __name__ == "__main__":
    run(botObj, TOKEN)


# @botObj.event
# async def on_message(ctx, message):
# 	check = lambda reaction, user: user == message.author and str(reaction.emoji) == ':zap:'
# 	try:
#         reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
#     except asyncio.TimeoutError:
#         await channel.send('```txt\nTimed Out\n```')
# 	else:
# 		code_run.runcode(ctx, message)
# https://discordpy.readthedocs.io/en/latest/api.html#discord.Message.add_reaction
