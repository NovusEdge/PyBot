import pathlib, base64
import os
import discord, json
from discord.ext import commands

from bot import botObj, TOKEN, run

path = pathlib.Path(__file__).parent.absolute()
os.chdir(path)
