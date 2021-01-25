import discord, json, base64, requests
import code, os, sys, timeit


def makeEmbed(output):
    bufFile = open("../embeds/code_run_embed.json", "w+")
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
                {
                    "name": "Output(stdout)",
                    "value": f"```txt\n{ output['stdout'] }\n```"
                },
                {
                    "name": "Error(stderr):",
                    "value": f"```txt\n{ output['stderr'] }\n```"
                },
                {
                    "name": "Error:",
                    "value": f"```txt\n{ output['error'] }\n```"
                }
        ]
    }
    print(embDict)
    json.dump(embDict, bufFile)
    bufFile.close()

def make_req(extn):
    code_file = open("BotCommands/buffer/code_run_inpcode", "r")
    resp_file = open("BotCommands/buffer/code_response.json", "w")
    langs = open("BotCommands/buffer/langs.json", "r")
    file_name = "main." + extn
    content = code_file.read()
    url, name = None, None

    for lang in json.load(langs):
        if extn in lang["prefix"]:
            name = lang["name"]
            url = lang["url"]
            break
    with open("BotCommands/code_config", "r") as f:
	    TOKEN = base64.b64decode(bytes(f.read().strip(), "utf-8")).decode('utf-8')

    headers = {
        "Authorization": f"Token {TOKEN}",
        'Content-type': 'application/json'
    }

    payload = {
        "data": {
            "files": [{"name": file_name, "content": f"{content}"}]
        }
    }

    if url:
        r = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)
        print(r.json())
        json.dump(r.json(), resp_file)

    code_file.close()
    resp_file.close()
    langs.close()

async def processCode(extn):
    make_req(extn)

    with open( "BotCommands/buffer/code_response.json", "r" ) as f:
        output = json.load(f)

    await makeEmbed(output)

async def sendEmbed(reaction):
    with open("../embeds/code_run_embed.json", "r") as f:
        embedObj = discord.Embed.from_dict(json.load(f))
        await reaction.message.channel.send(embed=embedObj)

async def runcode(reaction, user):
    msg = reaction.message
    with open("BotCommands/buffer/code_run_inpcode", "w+") as f:
        temp = msg.content.partition("\n")
        code = temp[2][:-3]
        extn = temp[0][3:]
        f.write(code)
    await processCode(extn)
    await sendEmbed(reaction)
