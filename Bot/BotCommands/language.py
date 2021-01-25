import requests, discord, json


async def languages(ctx):
    with open('../embeds/language_1.json', 'r') as f:
        emb1 = discord.Embed.from_dict(json.load(f)["embed"])

    with open('../embeds/language_2.json', 'r') as f:
        emb2 = discord.Embed.from_dict(json.load(f)["embed"])

    await ctx.send(embed=emb1)
    await ctx.send(embed=emb2)
