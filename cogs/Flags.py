from util.BotUtils import Utils
from util.BotUtils import nextcord
import nextcord
from nextcord.ext import commands
from util.ListUtils import COUNTRIES
import random


class Flags(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def flag(self, ctx):
        async with ctx.typing():
            flag = random.choice(COUNTRIES).lower()

            namefirst = flag.split(" ")[0]
            namespace = flag.replace(" ", "")
            print(flag)
            print("https://countryflagsapi.com/png/{}".format(flag))

            embed = nextcord.Embed(title = "Guess that flag!", colour = 0xff0000)
            embed.set_image(url = "https://countryflagsapi.com/png/{}".format(flag))

            await ctx.send(embed = embed)

        i=0
        while i < 63:
            message = await self.client.wait_for("message")
            msg = message.content.lower()
            if (msg == flag or msg == namefirst or msg == namespace):
                await Utils.generic_embed(ctx, title = f"Correct! {flag.title()}", desc = f"{message.author.name} got it!")
                break
            elif msg == "d!idk":
                await Utils.generic_embed(ctx, title = f"It's ||{flag.title()}!||")
                break
            elif msg == "d!hint":
                await Utils.generic_embed(ctx, title = f"It starts with the letter '{flag[0]}'")
            elif msg == "d!len":
                await Utils.generic_embed(ctx, title = f"It's name is {len(namefirst)} letters long")
            elif msg == "d!mon":
                break
            i+=1

def setup(client):
    client.add_cog(Flags(client))


