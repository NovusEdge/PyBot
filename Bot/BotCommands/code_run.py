import discord, json
import code, os, sys, StringIO

def getCode():
    with open("BotCommands/buffer/code_run_inpcode", "w") as codeFile:
        codeText = codeFile.read()
    return codeText


def makeEmbed(output):
    bufFile = open("BotCommands/buffer/code_run_embed.json", "w+")
    embDict = {
        "title": "Execution Complete",
        "color": 55807,
        "footer": {
          "text": "by PyBot"
          },
        "author": {
          "name": "PyBot",
          "icon_url": "https://raw.githubusercontent.com/NovusEdge/PyBot/master/logo(pexels-pixabay-247676).ico"
          },
        "fields": [
            "Output": f"```txt\n{ output[0] }\n```",
            "Error": f"```txt\n{ output[1] }\n```",
            ]
    }
    json.dump(embDict, bufFile)
    bufFile.close()


async def processCode(codeText):
    codeOut = StringIO.StringIO()
    codeErr = StringIO.StringIO()
    sys.stdout = codeOut
    sys.stderr = codeErr

    await exec codeText

    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__

    err = codeErr.getvalue()
    out = codeOut.getvalue()

    codeOut.close()
    codeErr.close()

    return out, err

# TODO: get the code with emoji/rxn and put in the buffer file

async def _runcode(ctx, message):
    codeFile = open("BotCommands/buffer/code_run_inpcode", "r")

    await output = processCode(getCode(message))
    makeEmbed(output)

    with open("BotCommands/buffer/code_run_embed.json", "r") as bufFile:
        embedObj = discord.Embed.from_dict( json.load(bufFile) )

    codeFile.close()
    await ctx.send(embed=embedObj)


async def runcode(ctx, message):
    message.clear_reaction(":zap:")
    message.add_reaction(":Loading:")
    _runcode(ctx, message)
    message.clear_reaction(":Loading:")
