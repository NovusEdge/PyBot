import requests, json, discord

async def cats(ctx):
    catPic = requests.get( 'https://api.thecatapi.com/v1/images/search' ).json()[0]['url']

    embedObj = discord.Embed.from_dict({
          "content": "Cat: ",
            "embed": {
                "title": "Here's a cute cat, Enjoy :hugging:",
                "color": 40447,
                "footer": {
                    "text": "Image by: https://apilist.fun/api/cats"
                    },
                "image": {
                    "url": f"{ catPic }"
                    },
                "author": {
                    "name": "PyBot",
                    "url": "https://discordapp.com",
                    "icon_url": "https://raw.githubusercontent.com/NovusEdge/PyBot/master/logo(pexels-pixabay-247676).ico"
                },
        "fields": [ ]
        }
    }['embed'])
    await ctx.send(embed=embedObj)
