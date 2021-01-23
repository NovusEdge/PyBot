import pathlib, base64, os, discord
from discord.ext import commands

path = pathlib.Path(__file__).parent.absolute()
os.chdir(path)

class PyBot(object):

    botObj = commands.Bot(command_prefix=">")

    def __init__(self, token, command_prefix=">"):
        self.token = token
        self.command_prefix = command_prefix
        self.botObj.command_prefix = command_prefix


    def run(self):
        while True:
            self.botObj.run(self.token)

    @botObj.event
    async def on_ready():
    	print('Bot Running')

    @botObj.command
    async def help():
        embedObj = discord.Embed.from_dict({
            title:
        })

if __name__ == "__main__":
    with open("config", "r") as f:
        TOKEN = base64.b64decode(bytes(f.read().strip(), "utf-8")).decode('utf-8')

    botObj = PyBot(command_prefix=">", token=TOKEN)
    botObj.run()
