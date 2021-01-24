import discord, json, os, base64, pathlib
from discord.ext import commands
from BotCommands import bot_help, code_run

path = pathlib.Path(__file__).parent.absolute()
os.chdir(path)

botObj =  commands.Bot(command_prefix=">", help_command=None)

@botObj.event
async def on_ready():
	print('Bot Running')

@botObj.command(aliases=["h"])
async def help(ctx):
	await bot_help.help(ctx)

@botObj.command(aliases=["rc", "run"])
async def runcode(ctx):
	await code_run.runcode(ctx)

def run(bot, token):
    bot.run(token)

with open("../config", "r") as f:
    TOKEN = base64.b64decode(bytes(f.read().strip(), "utf-8")).decode('utf-8')

if __name__ == "__main__":
    run(botObj, TOKEN)
