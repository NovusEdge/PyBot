import requests, discord

async def quote(ctx):
    r = requests.get('http://quotes.stormconsultancy.co.uk/random.json', 'r').json()

    embedObj = discord.Embed.from_dict({
          "content": "Quote: ",
            "embed": {
                "title": "Here's a random quote for ya :smiley:",
                "color": 40447,
                "footer": {
                    "text": "Quote from: http://quotes.stormconsultancy.co.uk"
                    },
                "author": {
                    "name": "PyBot",
                    "url": "https://discordapp.com",
                    "icon_url": "https://raw.githubusercontent.com/NovusEdge/PyBot/master/logo(pexels-pixabay-247676).ico"
                },
        "fields": [
            {
                "name": "Quote: ",
                "value": f"```\n{ r['quote'] }\n```"
            },
            {
                "name": "Author: ",
                "value": f"```\n{ r['author'] }\n```"
            }
        ]
        }
    }['embed'])
    await ctx.send(embed=embedObj)
